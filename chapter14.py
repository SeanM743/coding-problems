import collections

def is_btree_bst(tree):
    QueueEntry = collections.namedtuple('QueueEntry',('node', 'lower', 'upper'))

    bfsQueue = collections.deque(QueueEntry(tree, float('-inf'), float('inf'))

    while bfsQueue:
        curr_node = bfsQueue.popleft()
        if curr_node:
            if curr_node.lower >= curr_node.node.value >= curr_node.upper:
                return False
        bfsQueue += [QueueEntry(curr_node.node.left, curr_node.lower, curr_node.node.value),
                    QueueEntry(curr_node.node.right, curr_node.node.value, curr_node.upper)]
    
    return True

def first_node_greater(tree, value):
    candidate = None
    
    while tree:
        if tree.value > value:
            tree, candidate = tree.left, tree.value
        else:
            tree = tree.right
    
    return candidate

'''find the k largest elements in a bst'''

def k_largest_elements_bst(tree, k):

    results = []

    def k_large_helper(tree):
        if tree and len(results) < 3:
            k_large_helper(tree.right)
                if len(results) < 3:
                    results.add(tree.value)
                    k_large_helper(tree.left)
    
    k_large_helper(tree)
    return results

'''Compute the LCA in a BST'''

def compute_lca_bst(tree, node1, node2):
    larger_node, smaller_node = (node1, node2) if node1.value > node2.value else (node2,node1)
    
    while tree.value > larger_node.value or tree.value < smaller_node.value:
        while tree.value > larger_node.value:
            tree = tree.left
        while tree.value < smaller_node.value:
            tree = tree.right
    
    return tree

def reconstruct_bst_from_preorder(preorder_sequence):
    i = 0
    while preorder_sequence[i] <= preorder_sequence[0]:
        i += 1
    
    return BinaryNode(preorder_sequence[0], reconstruct_bst_from_preorder(preorder_sequence[1:i]), 
                        preorder_sequence[i:])

'''to improve runtime of the above, we can avoid recursing on elements repeatedly by adding a range'''

def reconstruct_bst_from_preorder_with_range(preorder_sequence):

    def reconstruct_helper(lower, upper):
        if root_idx = len(preorder_sequence):
            return None
            
        root = preorder_sequence[root_idx]
        if not lower <= root <= upper:
            return None
        root_idx += 1
        left = reconstruct_helper(lower, root)
        right = reconstruct_helper(root, upper)
        return BinaryNode(root, left, right)
    
    root_idx = 0
    reconstruct_helper(float('-inf'), float('inf'))

'''Use bintrees.RBTree to return closest entries in 3 sorted arrays'''

import bintree
def closest_entries(sorted_arrays):
    array_tree = bintree.RBTree()
    min_span = float('inf')

    for idx, sorted_array in enumerate(sorted_arrays):
        it = iter(sorted_array)
        array_tree.insert((next(it, None), idx), it)
    
    while True:
        min_element, min_idx = array_tree.min_key()
        max_element = array_tree.max_key()[0]
        min_span = min(max_element-min_element, min_span)
        it = array_tree.pop_min()[1]
        next_min = next(it, None)
        if not next_min:
            return min_span
        array_tree.insert(next_min, min_idx), it)
    
'''generate k smallest numbers from operation a + b*sqrt(2)'''

class ABSqrt2:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.val = a + b*sqrt(2)

    def __lt__(self, other):
        return self.val < other.val
    
    def __eq__(self, other):
        return self.val == other.val

def get_k_smallest_values(k):
    results = []
    #initiate the tree with smallest value (a=0, b= 0)
    candidates = bintree.RBTree([(ABSqrt2(0, 0), None)])
    while len(results) < k:
        next_min = candidates.pop_min()[0]
        results.append(next_min)
        candidates.insert([ABSqrt2(next_min.a + 1 + b*sqrt(2)), None])
        candidates.insert([ABSqrt2(next_min.a + (b+1)*sqrt(2)), None])
    return results

def generate_first_k_absqrt2(k):
    result = [ABSqrt2(0,0)]
    i = j = 0
    for _ in range(1, k):
        plus_i = ABSqrt2(result[i].a + 1, result[i].b)
        plus_j = ABSqrt2(result[j].a, result[j].b + 1)

        result.append(min(plus_i, plus_j))
        if plus_i <= result[-1]:
            i += 1
        if plus_j <= result[-1]:
            j += 1
    return result

def build_min_height_bst_from_sorted(A):
    def min_height_helper(A):
        if not A:
            return None
        root_idx = len(A)//2
        left = min_height_helper(A[0:root_idx])
        right = min_height_helper(A[root_idx + 1:])
        return BinaryNode(A[root_idx], left, right)
        
def proper_desc_ansc_of_middle(middle, possible1, possible2):

    search1, search2 = possible1, possible2

    while ((search1 or search2) and search1 not middle and search2 not middle and 
            search1 not possible2  and search2 not possible1):
        if search1:
            search1 = search1.left if search1.data < middle.data else search1.right
        if search2:
            search2 = search2.left if search2.data < middle.data else search2.right

    if (search1 not middle and search2 not middle) or search1 == possible2 or search2 == possible1:
        return False
    
    def search_from_middle(source, target):
        while source:
            source = source.left if source.value > target.value else source.right
        return source
    
    return search_from_middle(middle, possible1 if search1 == middle else possible2)

def node_successor(node):
    #if node.parent.left == node:   ###not needed because this case covered by return at end
    #    return node.parent    
    if node.right:
        node = node.right
        while node.left:
            node = node.left
        return node
    
    while node.parent and node.parent.right == node:
        node = node.parent
    
    return node.parent

Interval = collections.namedtuple('Interval',('low', 'high'))

def range_of_numbers_in_tree(node, R):
    
    def range_helper(node):
        if tree is None:
            return
        if R.low <= node.data <= R.high:
            result.append(node.data)
            range_helper(node.left)
            range_helper(node.right)
        elif R.low > node.data:
            range_helper(node.right)
        else: #R.high < node.data
            range_helper(node.left)
        
    result = []
    range_helper(node)
    return result

