# -*- coding: utf-8 -*-
"""
Created on Mon May 20 15:46:46 2019

@author: seanm
"""

def bsuccessors(state):
    here, there, t = state
    light = 'light'
    
    if light in here:
        return dict( ((frozenset(here - {a,b,'light'}), frozenset(there | {a,b,'light'}), max(a,b) + t) , (a,b,'->'))
                                            for a in here if a is not light
                                            for b in here if b is not light)
    else:
        return dict( ((frozenset(here | {a,b,'light'}), frozenset(there - {a,b,'light'}), max(a,b) + t) , (a,b,'<-'))
                                            for a in there if a is not light
                                            for b in there if b is not light)        
        

def test():

    assert bsuccessors((frozenset([1, 'light']), frozenset([]), 3)) == {
                (frozenset([]), frozenset([1, 'light']), 4): (1, 1, '->')}

    assert bsuccessors((frozenset([]), frozenset([2, 'light']), 0)) =={
                (frozenset([2, 'light']), frozenset([]), 2): (2, 2, '<-')}
    
    return 'tests pass'

def bridge_problem(here):
    
    start = (frozenset(here) | frozenset(['light']),frozenset([]),0)
    frontier = [[start]]
    explored = set()
    
    if not here:
        return frontier[0]
    
    while frontier:
        path = frontier.pop(0)
        for (state,action) in bsuccessors(path[-1]).items():
            
            if state not in explored:
                path2 = path + [action,state]
                here,there,t = state
                explored.add(state)
                if not here:
                    return path2
                else:
                    frontier.append(path2)
                    frontier.sort(key = lambda p: p[-1][2])
    return []
                
#print(bridge_problem([1,2,5,10]))                

def bridge_problem2(here):
    """Modify this to test for goal later: after pulling a state off frontier,
    not when we are about to put it on the frontier."""
    ## modify code below
    here = frozenset(here) | frozenset(['light'])
    explored = set() # set of states we have visited
    # State will be a (people-here, people-there, time-elapsed)
    frontier = [ [(here, frozenset(), 0)] ] # ordered list of paths we have blazed
    if not here:
        return frontier[0]
    while frontier:
        path = frontier.pop(0)
        if not path[-1][0]:
            return path
        for (state, action) in bsuccessors(path[-1]).items():
            if state not in explored:
                here, there, t = state
                explored.add(state)
                path2 = path + [action, state]
                frontier.append(path2)
                frontier.sort(key=lambda p: p[-1][2])
    return []

def test2():
    assert bridge_problem2(frozenset((1, 2),))[-1][-1] == 2 # the [-1][-1] grabs the total elapsed time
    assert bridge_problem2(frozenset((1, 2, 5, 10),))[-1][-1] == 17
    return 'tests pass'

#print(test2())


#the problem with the above implementation is it is very inefficient and allows for (here,there,t) combinations to represent variations
# of the same state. For example, ((1,2),(3),3) would be a different state from ((1,2),(3),5) even though it has the same here/there values
    #to correct this I will implement a new definition of state to be just (here,there) and incorporate t into the path variable
    
def bsuccessors2(state):
    """Return a dict of {state:action} pairs. A state is a
    (here, there) tuple, where here and there are frozensets
    of people (indicated by their travel times) and/or the light."""
    here,there = state
    
    light = 'light'
    
    if light in here:
        return dict(( (here - frozenset([a,b,'light']), there | frozenset([a,b,'light'])),
                    (a,b,'->')) for a in here if a is not light
                                for b in here if b is not light)
    else:
        return dict(( (here | frozenset([a,b,'light']) , there - frozenset([a,b,'light'])),
                    (a,b,'<-')) for a in there if a is not light
                                for b in there if b is not light)            

def test_suc2():
    here1 = frozenset([1, 'light']) 
    there1 = frozenset([])

    here2 = frozenset([1, 2, 'light'])
    there2 = frozenset([3])
    
    assert bsuccessors2((here1, there1)) == {
            (frozenset([]), frozenset([1, 'light'])): (1, 1, '->')}
    assert bsuccessors2((here2, there2)) == {
            (frozenset([1]), frozenset(['light', 2, 3])): (2, 2, '->'), 
            (frozenset([2]), frozenset([1, 3, 'light'])): (1, 1, '->'), 
            (frozenset([]), frozenset([1, 2, 3, 'light'])): (2, 1, '->')}
    return 'tests pass'
#print(test_suc2())
    


def path_cost(path):
    """The total cost of a path (which is stored in a tuple
    with the final action."""
    # path = (state, (action, total_cost), state, ... )
    if len(path) < 3:
        return 0
    else:
        return path[-2][1]
        
def bcost(action):
    """Returns the cost (a number) of an action in the
    bridge problem."""
    # An action is an (a, b, arrow) tuple; a and b are 
    # times; arrow is a string. 
    a, b, arrow = action
    return max(a,b)

def test_cost():
    assert path_cost(('fake_state1', ((2, 5, '->'), 5), 'fake_state2')) == 5
    assert path_cost(('fs1', ((2, 1, '->'), 2), 'fs2', ((3, 4, '<-'), 6), 'fs3')) == 6
    assert bcost((4, 2, '->'),) == 4
    assert bcost((3, 10, '<-'),) == 10
    return 'tests pass'

print(test_cost())








