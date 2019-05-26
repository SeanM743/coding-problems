# -*- coding: utf-8 -*-
"""
Created on Wed May 22 14:58:36 2019

@author: seanm

This file builds a generalized shortest path search algorithm. It will
contain the following concepts:
    1) paths: [state,action,state...]
    2) states: atomic, don't need to know how these work in main fun
    3) actions: also atomic
    4) successor(state) returns state,action dictionary
    5) start: starting state that is atomic
    6) goal state: function since it could include multiple states,
    returns a boolean

main function is shortest_path_search(successor,start,goal) -> path
"""

def shortest_path_search(start, successors, is_goal):
    """Find the shortest path from start state to a state
    such that is_goal(state) is true."""
    
    if(is_goal(start)):
        return start
        
    explored = {}
    frontier = [[start]]
    path = []
    
    while frontier:
        path = frontier.pop(0)
        s = path[-1]
        for state,action in successors(s).items:
            if state not in explored:
                explored.add(state)
                path2 = path + [state,action]
                if is_goal(state):
                    return path2
                else:
                    frontier.append(path2)
    return None
    
    
    
    
    
    