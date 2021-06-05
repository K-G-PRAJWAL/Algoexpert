# Solution 1: Recursive approach
def binarySearch(array, target):
    '''
    Time: O(log(n))
    Space: O(log(n))
    '''
    return binarySearchHelper(array, target, 0, len(array) - 1)


def binarySearchHelper(array, target, left, right):
    if left > right:
        return - 1
    middle = (left + right) // 2
    potentialMatch = array[middle]
    if target == potentialMatch:
        return middle
    elif target < potentialMatch:
        return binarySearchHelper(array, target, left, middle - 1)
    else:
        return binarySearchHelper(array, target, middle + 1, right)


# Solution 2: Iterative approach
def binarySearch(array, target):
    '''
    Time: O(log(n))
    Space: O(1)
    '''
    return binarySearchHelper(array, target, 0, len(array) - 1)


def binarySearchHelper(array, target, left, right):
    while left <= right:
        middle = (left + right) // 2
        potentialMatch = array[middle]
        if target == potentialMatch:
            return middle
        elif target < potentialMatch:
            right = middle-1
        else:
            left = middle+1
    return -1


print(binarySearch([2, 4, 90, 99, 1001, 100023], 1001))
