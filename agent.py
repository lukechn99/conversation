from typing import List

class agent:
    def __init__(self, name, engagement, attributes):
        self.name = name
        self.engagement = engagement
        self.attributes = attributes

    def get_attributes(self) -> List[str]:
        return self.attributes

    def add_attribute(self, attribute):
        self.attributes.append(attribute)

    def get_engagement(self):
        return self.engagement

    def modify_engagement(self, amount):
        self.engagement += amount

    def get_name(self):
        return self.name

    def can_relate(self, topic):
        '''
        We can alter this to use more realistic styles of topic matching later
        '''
        if topic in self.attributes:
            return True
        return False

    def talk_about(self, topic):
        pass