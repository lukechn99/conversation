# conversation

Given two agents and a slew of different attributes that interact in an intricate network, we can create social interaction. Social interaction, in this simulation can be summed up as two agents who try to find a common attribute. Attributes lend themselves to conversation and can lead to other attributes based on how they are connected in an agent's personality network. If attribute networks are a good match between two agents, then they can continue navigating through and making conversation. When they hit a dead end, where either an attribute is depleted or their personality networks reach a point of not matching, then conversation should resolve back down the conversation stack.  

Take for example the following representations:  
```
class attribute:
    connections<>
```
```
class person:
    attributes<>
    engagement
```
```
class conversation:
    people<>
```  
---
For agent A and agent B
```
agent A:
    attributes = <tennis, piano, classical painting, student, daughter>
    engagement = 1

agent B:
    attributes = <cooking, badminton, classical violin, abstract artist, father>
    engagement = 1
```
Those attributes could have a network like so:  
```
tennis:
    connections = <badminton>
piano:
    connections = <classical painting, classical violin>
classical painting:
    connections = <classical violin, abstract artist>
student:
    connections = <piano, tennis, badminton, classical violin>
daughter:
    connections = <father>
cooking:
    connections = <>
badminton:
    connections = <tennis>
classical violin:
    connections = <classical painting, piano>
abstract artist:
    connections = <classical painting>
father:
    connections = <daughter, student, cooking>
```
A conversation between two agents might look like...

### 
