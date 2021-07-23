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
    attributes = <tennis, piano, classical painting, student, daughter, cooking>
    engagement = 1

agent B:
    attributes = <badminton, classical violin, abstract artist, father, tennis, cooking>
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
A conversation between two agents might look like this:
```
A: Hi, I'm a father and artist who likes to cook, enjoy listening to classical violin, and play tennis and badminton in my free time
B: I also like to cook!
A: What do you typically cook?
B: I make Peruvian food
A: Cool, I like to each American BBQ
// at this point, cooking is low on their list of attributes and it has no other attributes that branch off from it, so the conversation stack goes back to A's initial introduction
// A's engagement level: 1.0 -> 0.8
// B's engagement level: 1.0 -> 0.9
B: You said you like classical violin right? I love to play piano
A: How long have you played? I like classical violin from Bach's era
B: I've played for 10 years now. I'm performing an open recital that you could come to! My dad is coming.
A: I would enjoy that very much. I often go watch my son's tennis matches; he's a student at North High School.
B: My school has played against that school! (Student) I also like tennis (Tennis), but my main sport is badminton.
// at this point, A and B have been building up the conversation stack which will resolve itself when the topmost attribute is depleted and there is no further connection to explore
// A's engagement level: 0.8 -> 1.1
// B's engagement level: 0.9 -> 1.0
```
The conversation stack so far would look something like this:
```



                    ->                      ->                      ->                      ->
                        [     cooking    ]                              [classical violin]
[A's introduction]      [A's introduction]      [A's introduction]      [A's introduction]

                                                                        [     tennis     ]      
                                                [     father     ]      [     father     ]    
                        [    daughter    ]      [    daughter    ]      [    daughter    ]      
[classical piano ]  ->  [classical piano ]  ->  [classical piano ]  ->  [classical piano ]  ->    
[classical violin]      [classical violin]      [classical violin]      [classical violin]      
[A's introduction]      [A's introduction]      [A's introduction]      [A's introduction]      

                        [     student    ]                              [    badminton   ]
[     tennis     ]      [     tennis     ]      [     tennis     ]      [     tennis     ]
[     father     ]      [     father     ]      [     father     ]      [     father     ]
[    daughter    ]      [    daughter    ]      [    daughter    ]      [    daughter    ]
[classical piano ]  ->  [classical piano ]  ->  [classical piano ]  ->  [classical piano ]  ->
[classical violin]      [classical violin]      [classical violin]      [classical violin]
[A's introduction]      [A's introduction]      [A's introduction]      [A's introduction]
```

### 
