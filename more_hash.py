'''design an algorithm that finds the LCA of two nodes in a binary tree whose complexity only depends on the distance between the two nodes'''

def node_lca(node1, node2):
    iter1, iter2 = node1, node2
    nodes_visited = set()

    while iter1 or iter2:

        if iter1:
            if iter1 in nodes_visited:
                return iter1
            nodes_visted.add(iter1)
            iter1 = iter1.parent

        if iter2:
            if iter2 in nodes_visited:
                return iter2
            nodes_visited.add(iter2)
            iter2 = iter2.parent

    return False

'''find shortest distance between two duplicate words in a string'''
def word_distance(s):
    distances, nearest_word_distance = {}, math.inf

    for idx, word in enumerate(s):
        if word in distances:
            d = idx - distances[word]
            nearest_word_distance = min(nearest_word_distance, d)
        distances[word] = idx
    
        return nearest_word_distance


'''find the shortest distance between a set of keywords in a string (paragraph)
Example: 
String = 'cat dog dog mouse bird cat elephant'
Keywords = 'cat', 'mouse'
Shortest distance is element 0 to element 3'''

import collections

def shortest_keywords_len(para, keywords):

    #strategy is to move along paragraph until all keywords covered, then advance left pointer until set is uncovered
    #compare this to stored minimum distance and replace if lower
    #continue to advance in the paragraph, but now we can start at the right pointer since we know nothing shorter between left and right

    count_of_keywords = collections.Counter(keywords)
    print(count_of_keywords)
    result = (-1, -1)
    left = 0
    remaining_keywords = len(keywords)

    for right, word in enumerate(para):
        if word in keywords:
            count_of_keywords[word] -= 1
            if count_of_keywords[word] >= 0:
                remaining_keywords -= 1
        
        while(remaining_keywords == 0):
            if result == (-1, -1) or right - left < result[1] - result[0]:
                result = (left,right)

            if para[left] in keywords:
                count_of_keywords[para[left]] += 1
                if count_of_keywords[para[left]] > 0:
                    remaining_keywords += 1
            
            left += 1

    return result

a = ['apple','banana','dog']
b = ['apple','cat']
print(shortest_keywords_len(a,b))