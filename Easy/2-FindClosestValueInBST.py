# def findClosestValueInBST(tree, target):
#     '''
#     Recursive Approach
#     Average time: O(log(n)) | Average space: O(log(n))
#     Worst time: O(n) | Worst space: O(n)
#     '''
#     return findClosestValueInBSTHelper(tree, target, float("inf"))


# def findClosestValueInBSTHelper(tree, target, closest):
#     if tree is None:
#         return closest
#     if abs(target-closest) > abs(target-tree.value):
#         closest = tree.value
#     if target < tree.value:
#         return findClosestValueInBSTHelper(tree.left, target, closest)
#     elif target > tree.value:
#         return findClosestValueInBSTHelper(tree.right, target, closest)
#     else:
#         return closest

def findClosestValueInBST(tree, target):
    '''
    Iterative Approach
    Average time: O(log(n)) | Average space: O(1)
    Worst time: O(n) | Worst space: O(1)
    '''
    return findClosestValueInBSTHelper(tree, target, float("inf"))


def findClosestValueInBSTHelper(tree, target, closest):
    curr = tree
    while curr is not None:
        if abs(target-closest) > abs(target-curr.value):
            closest = curr.value
        if target < curr.value:
            curr = curr.left
        elif target > curr.value:
            curr = curr.right
        else:
            break
    return closest
