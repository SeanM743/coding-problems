# -*- coding: utf-8 -*-
"""
Created on Tue May 21 10:42:13 2019

@author: seanm
"""
#cannibal problem where missionaries and cannibals are trying to cross a stream in a boat. If the cannibals outnumber the missionaries, then
#the missionaries will be eaten


def csuccessors(state):
    """Find successors (including those that result in dining) to this
    state. But a state where the cannibals can dine has no successors."""
    M1, C1, B1, M2, C2, B2 = state
    
    if C1 > M1 > 0 or C2 > M2 > 0:
        return {}
    items = []
    
    d = {(1, 0, 1, -1, 0, -1): 'M',
          (2, 0, 1, -2, 0, -1): 'MM',
          (1, 1, 1, -1, -1, -1): 'MC',
          (0, 1, 1, 0, -1, -1): 'C',
          (0, 2, 1, 0, -2, -1): 'CC'}
    
    if B1:
        items += [(sub(state,delta), a + '->') for delta,a in d.items()]
    else:
        items+= [(add(state,delta), '<-'+a) for delta,a in d.items()]
    

    return dict(items)

def sub(state,delta):
    return tuple(x-y for x,y in zip(state,delta))

def add(state,delta):
    return tuple(x+y for x,y in zip(state,delta))
        
def test():
    assert csuccessors((2, 2, 1, 0, 0, 0)) == {(2, 1, 0, 0, 1, 1): 'C->', 
                                               (1, 2, 0, 1, 0, 1): 'M->', 
                                               (0, 2, 0, 2, 0, 1): 'MM->', 
                                               (1, 1, 0, 1, 1, 1): 'MC->', 
                                               (2, 0, 0, 0, 2, 1): 'CC->'}
    assert csuccessors((1, 1, 0, 4, 3, 1)) == {(1, 2, 1, 4, 2, 0): '<-C', 
                                               (2, 1, 1, 3, 3, 0): '<-M', 
                                               (3, 1, 1, 2, 3, 0): '<-MM', 
                                               (1, 3, 1, 4, 1, 0): '<-CC', 
                                               (2, 2, 1, 3, 2, 0): '<-MC'}
    assert csuccessors((1, 4, 1, 2, 2, 0)) == {}
    return 'tests pass'

#print(test())
    
def boat_cross(start = (3,3,1,0,0,0), goal = None):
    if goal is None:
        goal = (0,0,0) + start[:3]
    if goal == start:
        return start
    
    explored = {}
    path = []
    frontier = [[start]]
    
    while frontier:
        path = frontier.pop(0)
        for (state,action) in csuccessors(path[-1]).items():
            if state not in explored:
                explored.add(state)
                path2 = path + [state,action]
                if path2 == goal:
                    return path2
                path.append(path2)
        
    return None
    
    
    
    
    
    
    
