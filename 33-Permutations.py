# Solution 1
def Permutations(array):
    '''
    Time: O(N^2.N!)
    Space: O(N.N!)
    '''
    permutations = []
    permutationsHelper(array, [], permutations)
    return permutations


def permutationsHelper(arr, currPerm, permutations):
    if not len(arr) and len(currPerm):
        permutations.append(currPerm)
    else:
        for i in range(len(arr)):
            newArr = arr[:i]+arr[i+1:]
            newPerm = currPerm + [arr[i]]
            permutationsHelper(newArr, newPerm, permutations)


# Solution 2
def Permutations(array):
    '''
    Time: O(N.N!)
    Space: O(N.N!)
    '''
    permutations = []
    permutationsHelper(0, array, permutations)
    return permutations


def permutationsHelper(i, array, permutations):
    if i == len(array)-1:
        permutations.append(array[:])
    else:
        for j in range(i, len(array)):
            array[i], array[j] = array[j], array[i]
            permutationsHelper(i + 1, array, permutations)
            array[i], array[j] = array[j], array[i]


print(Permutations([1, 2, 3, 3]))
