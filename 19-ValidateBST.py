def validateBST(tree):
    '''
    Time: O(n)
    Space: O(depth of the tree)
    '''
    return validateBSTHelper(tree, float("-inf"), float("inf"))


def validateBSTHelper(tree, mini, maxi):
    if tree is None:
        return True
    if tree.value < mini or tree.value >= maxi:
        return False
    leftIsValid = validateBSTHelper(tree.left, mini, tree.value)
    return leftIsValid and validateBSTHelper(tree.right, tree.value, maxi)
