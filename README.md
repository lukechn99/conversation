# conversation

Given two agents and a slew of different attributes that interact in an intricate network, we can create social interaction. Social interaction, in this simulation can be summed up as two agents who try to find a common attribute. Attributes lend themselves to conversation and can lead to other attributes based on how they are connected in an agent's personality network. If attribute networks are a good match between two agents, then they can continue navigating through and making conversation. When they hit a dead end, where either an attribute is depleted or their personality networks reach a point of not matching, then conversation should resolve back down the conversation stack.  

Take for example the following representations  
```
class attribute:
    connections<>
    importance
```
```
class person:
    attributes<>
```
```
class conversation:
    people<>
    engagement
```  
