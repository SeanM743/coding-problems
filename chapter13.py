'''Write a function that determines the smallest value that cannot be
achieved with a set of coins. For example, if you have the following coins:
1, 2, 2, 7 you can make the values 1 through 9, so the smallest value
that cannot be achieved is 10 cents. Assume the array is sorted'''

def smallest_denom(coins):

    total = 0
    for i, val in enumerate(coins):
        total += val
        if val > total + 1:
            return total + 1
    return sum(coins) + 1

'''Inputs: tuple of events of start and end times for appointments 
        in the calendar
   Outputs: Max number of concurrent appointments'''

import collections
Event = collections.namedtuple('Event', ('start','end'))

def max_concurrent(calendar):
    Endpoint = collections.namedtuple('Endpoint', ('time','isEnd'))

    endpoints = ([Endpoint(event.start, False) for event in calendar] + 
                 [Endpoint(event.end, True) for event in calendar])
    
    #sort the endpoints by time, breaking ties by putting start first
    endpoints.sort(key = lambda e: (e.time, e.isEnd))
    max_sim_events, num_events = 0, 0
    for endpoint in endpoints:
        if not endpoint.isEnd:
            num_events += 1
            max_sim_events = max(max_sim_events,num_events)
        elif endpoint.isEnd:
            num_events -= 1
    
    return max_sim_events

# calendar = [Event('0800', '0900'), Event('0830','1000'), Event('0900','1100')]

# print(max_concurrent(calendar))


#Interval = collections.namedtuple('Interval',('start', 'end'))

def merge_intervals(disjoint_intervals, new_interval):
    i, results = 0, []

    def union(interval1, interval2):
        return Interval( min(interval1.start, interval2.start), 
               max(interval1.end, interval2.end))
    
    while i < len(disjoint_intervals) and disjoint_intervals[i].end < new_interval.start:
        i += 1
        results.append(disjoint_intervals[i])
    
    while i < len(disjoint_intervals) and new_interval.end >= disjoint_intervals[i].start:
        new_interval = union(new_interval, disjoint_intervals[i])
    
    return results + [new_interval] + disjoint_intervals[i:]

Endpoints = collections.namedtuple('Endpoint', ('is_closed', 'val'))

class Interval:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def __lt__(self,other):
        if self.left.val != other.left.val:
            return self.left.val < other.left.val
        return self.left.is_closed and not other.left.is_closed

def union_of_intervals(intervals):
    intervals.sort()
    result = [intervals[0]]

    for i in intervals:
        if (i.left.val < result[-1].right.val or (i.left.val == result[-1].right.val and
            (i.left.is_closed or result[-1].right.is_closed))):
            if (i.right.val > result[-1].right.val or (i.right.val == result[-1].right.val and
               i.right.is_closed)):
               result[-1].right = i.right 
        else:
            result.append(i)
    return result

'''check if players on opposing teams can be arranged so that taller player is behind the shorter one'''

Player = collections.namedtuple('Player',('height'))

class Team:
    def __init__(self, heights):
        self._players = [Player(h) for h in heights]

def valid_placement_exists(team1, team2):
    team1._players.sort(key = lambda p: p.height)
    team2._players.sort(key = lambda p: p.height)

    #return all(a.height < b.height for a,b in zip(team1, team2))
    return all(a < b for a, b in zip(team1._players, team2._players))

h1 = [1,5,7,9]
h2 = [2, 10, 6, 12]

team1 = Team(h1)
team2 = Team(h2)
print(valid_placement_exists(team2, team1))

def insertion_sort(L):
    dummy_head = LinkedNode(0, L)

    while(L and L.next):
        if L.data > L.next.data:
            target, pre = L.next, dummy_head
            while target.data > pre.next.data:
                pre = pre.next
            temp = pre.next
            pre.next = target
            L.next = target.next
            target.next = temp
        else:
            L = L.next

    return dummy_head.next

            
