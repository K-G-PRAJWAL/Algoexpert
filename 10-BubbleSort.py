def bubbleSort(array):
    '''
    Time: O(n^2)
    Space: O(1)
    '''
    isSorted = False
    counter = 0
    while not isSorted:
        isSorted = True
        for i in range(len(array) - 1 - counter):
            if array[i] > array[i + 1]:
                array[i], array[i+1] = array[i+1], array[i]
                isSorted = False
        counter += 1
    return array


print(bubbleSort([8, 7, 9, 10, -1, 11, 2, -9]))
