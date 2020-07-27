def kadanesalgorithm(array):
    '''
    Time: O(N)
    Space: O(1)
    '''
    localMaxima = array[0]
    globalMaxima = array[0]
    for i in range(1, len(array)):
        localMaxima = max(array[i], array[i] + localMaxima)
        globalMaxima = max(localMaxima, globalMaxima)
    return globalMaxima


print(kadanesalgorithm([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]))
