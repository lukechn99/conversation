from agent import agent
from topic_content import topic_content
from conversation_stack import conversation_stack
from typing import List, Dict

import requests
import json
import logging

'''
Resources
https://en.wikipedia.org/w/api.php?action=help&modules=query%2Bextracts
https://www.mediawiki.org/wiki/API:Search
'''

logging.basicConfig(filename='conversation_run.log', filemode='w',
                    format='%(name)s - %(levelname)s - %(asctime)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

FILE = "agents.json"

# load agents
"""
CONVERSATION
conversation should flow simply...

I like ...
That's very cool, I like ...


"""

"""
How to fuzzy match terms?

"""

# come up with core topics and map each topic to a core
# then when matching conversation topics, check for core instead of 
# doing exact match

def load_article(topic: str) -> topic_content:
    '''
    uses http request to grab page contents from Wikipedia for the query "topic" 
    and returns the results
    '''
    requests_session = requests.Session()

    URL = "https://en.wikipedia.org/w/api.php"

    PARAMS = {
        "action": "query",
        "exchars": 300,
        "prop": "extracts",
        "format": "json",
        "explaintext": True,
        "titles": topic
    }

    response = requests_session.get(url=URL, params=PARAMS)
    response_json = response.json()

    id = list(response_json["query"]["pages"].keys())[0]
    contents = response_json["query"]["pages"][id]["extract"]
    
    topic_content_obj = topic_content(topic, json.dumps(contents, indent=4))
    
    logger.info("fetched the {} article".format(topic))
    return topic_content_obj


def load_agents() -> List[agent]:
    agents = []
    try:
        with open(FILE, 'r') as f:
            data = json.load(f)
            for entry in list(data.keys()):
                new_agent = agent(
                    entry, data[entry]["engagement"], data[entry]["attributes"])
                agents.append(new_agent)
        logger.info("successfully imported agents")
        return agents
    except Exception as e:
        logger.error(str(e))
        return []


def converse(agents: List[agent]):
    if not agents:
        logger.info("no agents found")
        pass

    logger.info("loading agents")
    conversation = conversation_stack()

    # load a random first topic
    conversation.push(agents[0].get_attributes()[0])
    logger.info("pushed first topic {}".format(conversation.peek()))

    while conversation.is_not_empty():
        current_topic = conversation.peek()
        logger.info("starting discussion on {}".format(current_topic))
        # we default to having no one engage with the topic
        engaged = False

        for agent in agents: 
            # if agent can relate to the current topic, say something
            # and add topic to conversation
            if agent.can_relate(current_topic):
                agent.talk_about(current_topic)
                conversation.push(current_topic)
                engaged = True
            # else move onto next agent

        if not engaged:
            # decrease each agent's engagement
            for agent in agents:
                agent.modify_engagement(-2)
                if agent.get_engagement() <= 0:
                    # TODO remove agent from conversation
                    pass
            # pop the topic
            conversation.pop()

    # rotate through the agents to offer new topics if the stack runs out
    for agent in agents:
        if conversation:
            pass


def main():
    logger.info("starting conversation")
    agents = load_agents()
    converse(agents)


main()