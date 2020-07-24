def selectionSort(array):
    '''
    Time: O(n^2)
    Space: O(1)
    '''
    curr = 0
    while curr < len(array) - 1:
        smallest = curr
        for i in range(curr + 1, len(array)):
            if array[smallest] > array[i]:
                smallest = i
        array[curr], array[smallest] = array[smallest], array[curr]
        curr += 1
    return array


print(selectionSort([-1, -999, 100, -101, 1001, 68, 3, 45, -1001]))
