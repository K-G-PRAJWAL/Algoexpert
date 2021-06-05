'''
All three functions have the following complexity:
Time: O(n)
Space: O(n, depth of BST)
'''


def inOrder(tree, array):
    if tree is not None:
        inOrder(tree.left, array)
        array.append(tree.value)
        inOrder(tree.right, array)
    return array


def preOrder(tree, array):
    if tree is not None:
        array.append(tree.value)
        preOrder(tree.left, array)
        preOrder(tree.right, array)
    return array


def postOrder(tree, array):
    if tree is not None:
        postOrder(tree.left, array)
        postOrder(tree.right, array)
        array.append(tree.value)
    return array
