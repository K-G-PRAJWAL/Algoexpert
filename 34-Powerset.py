# Solution 1
# def powerset(array):
#     '''
#     Time: O(N.2^N)
#     Space: O(N.2^N)
#     '''
#     subset = [[]]
#     for element in array:
#         for i in range(len(subsets)):
#             currSubset = subset[i]
#             subset.append(currSubset+[element])
#     return subsets


# Solution 2
def powerset(array, i=None):
    '''
    Time: O(N.2^N)
    Space: O(N.2^N)
    '''
    if i == None:
        i = len(array) - 1
    elif i < 0:
        return [[]]
    ele = array[i]
    subset = powerset(array, i - 1)
    for j in range(len(subset)):
        currSubset = subset[j]
        subset.append(currSubset + [ele])
    return subset


print(powerset([1, 2, 3]))
