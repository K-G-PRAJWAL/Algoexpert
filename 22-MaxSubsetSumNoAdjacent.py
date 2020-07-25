# Solution 1
# def maxSubsetSumNoAdjacent(array):
#     '''
#     Time: O(n)
#     Space: O(n)
#     '''
#     if not len(array):
#         return
#     elif len(array) == 1:
#         return array[0]
#     maxSums = array[:]
#     maxSums[1] = max(array[0], array[1])
#     for i in range(2, len(array)):
#         maxSums[i] = max(maxSums[i - 1], maxSums[i - 2] + array[i])
#     return maxSums[-1]


# Solution 2
def maxSubsetSumNoAdjacent(array):
    '''
    Time: O(n)
    Space: O(1)
    '''
    if not len(array):
        return
    elif len(array) == 1:
        return array[0]
    second = array[0]
    first = max(array[0], array[1])
    for i in range(2, len(array)):
        curr = max(first, second + array[i])
        second = first
        first = curr
    return first


print(maxSubsetSumNoAdjacent([7, 10, 12, 7, 9, 14]))
