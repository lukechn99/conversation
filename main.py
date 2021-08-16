from agent import agent
from typing import List

import json
import logging
logging.basicConfig(filename='app.log', filemode='w',
                    format='%(name)s - %(levelname)s - %(asctime)s - %(message)s', level=logging.INFO)
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


def load_agents() -> List[agent]:
    agents = []
    try:
        with open(FILE, 'r') as f:
            data = json.load(f)
            for entry in list(data.keys):
                new_agent = agent(
                    entry, data[entry]["engagement"], data[entry]["attributes"])
                agents.append(new_agent)
        return agents
    except Exception as e:
        logger.error(str(e))
        return []


def converse(agents: List[agent]):
    if not agents:
        pass
    conversation_stack = []

    # rotate through the agents to offer new topics if the stack runs out
    for agent in agents:
        if conversation_stack:
            pass


def main():
    agents = load_agents()
    converse(agents)
