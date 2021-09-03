from typing import Dict

class topic_content:
    '''
    Somehow I need to extract and map key terms in the topic content so that 
    the topic can be easily matched with another topic
    '''
    def __init__ (self, _topic_name: str, _contents: Dict[str, str]):
        self.topic_name = _topic_name
        self.contents = _contents