'''implement an inorder traversal of a binary tree recursively and iteratively'''

def rec_inorder_traversal(tree):
    if not tree:
        return
    
    rec_inorder_traversal(tree.left)
    print(tree.data)
    rec_inorder_traversal(tree.right)

def iter_inorder_traversal(tree):

    stack_nodes = []
    result = []

    while tree or stack_nodes:

        if tree:
            stack_nodes.append(tree)
            tree = tree.left
        
        elif stack_nodes:
            tree = stack_nodes.pop()
            result.append(tree.value)
            tree = tree.right
    
    return result

'''Implement a preorder traversal of a binary tree: Root - Left - Right'''

def iter_preorder(tree):

    path, result = [tree],[]

    while path:
        curr = path.pop()
        result.append(curr.value)
        if curr:
            path += [curr.right,curr.left]

''' write a function that finds the kth node in an inorder traversal. Assum that each node stores information about the number
of nodes in its subtree'''

def kth_node(tree,k):

    while tree:
        if k == 0:
            return tree.value

        if tree.left.num_nodes < k:
            k = k - tree.right.num_nodes
            tree = tree.right
        elif tree.left.num_nodes > k:
            k -= 1
            tree = tree.left

def successor(node):
    '''Return successor node for an inorder traversal. Efficiency noted here is that if there is a right subtree, the next node
    will be the left most node of the right subtree'''

    if node.right:
        while node.left:
            node = node.left
        return node

    while node.parent and node.parent.right == node:
        node = node.parent
    
    return node.parent






    