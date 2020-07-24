def insertionSort(array):
    '''
    Time: O(n^2)
    Space: O(1)
    '''
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j-1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1
    return array


print(insertionSort([2, -1, 10, 999, 1, 1001, 399]))
