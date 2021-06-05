# Solution 1 - Iterative Solution
def invertBinaryTree(tree):
    '''
    Time: O(n)
    Space: O(n)
    '''
    queue = [tree]
    while len(queue):
        curr = queue.pop(0)
        if curr is None:
            continue
        tree.left, tree.right = tree.right, tree.left
        queue.append(curr.left)
        queue.append(curr.right)


# Solution 2 - Recursive Solution
def invertBinaryTree(tree):
    '''
    Time: O(n)
    Space: O(depth of tree)
    '''
    if tree is None:
        return
    tree.left, tree.right = tree.right, tree.left
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)
