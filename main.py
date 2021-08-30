from agent import agent
from typing import List, Dict

import requests
import json
import logging

'''
Resources
https://en.wikipedia.org/w/api.php?action=help&modules=query%2Bextracts
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

class topic_content:
    '''
    Somehow I need to extract and map key terms in the topic content so that 
    the topic can be easily matched with another topic
    '''
    def __init__ (self, _topic_name: str, _contents: Dict[str, str]):
        self.topic_name = _topic_name
        self.contents = _contents


class conversation_stack:
    '''
    check size before popping
    '''
    def __init__(self, stack=[]):
        self.stack = stack

    def push(self, item: str):
        self.stack.append(item)

    def pop(self) -> str:
        return self.stack.pop()

    def size(self) -> int:
        return len(self.stack)

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
    conversation.push("none")
    for agent in agents:
        for attr in agent.get_attributes():
            print(load_article(attr).contents)

    # rotate through the agents to offer new topics if the stack runs out
    for agent in agents:
        if conversation:
            pass


def main():
    logger.info("starting conversation")
    agents = load_agents()
    converse(agents)


main()