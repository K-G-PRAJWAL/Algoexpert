def quickSort(array):
    '''
    Time: O(nlog(n))
    Space: O(log(n))
    '''
    quickSortHelper(array, 0, len(array) - 1)
    return array


def quickSortHelper(array, start, end):
    if start > end:
        return
    pivot = start
    left = start + 1
    right = end
    while right >= left:
        if array[left] > array[pivot] and array[right] < array[pivot]:
            array[left], array[right] = array[right], array[left]
        if array[left] <= array[pivot]:
            left += 1
        if array[right] >= array[pivot]:
            right -= 1
    array[pivot], array[right] = array[right], array[pivot]
    leftarray = right - 1 - start < end - (right + 1)
    if leftarray:
        quickSortHelper(array, start, right - 1)
        quickSortHelper(array, right + 1, end)
    else:
        quickSortHelper(array, right+1, end)
        quickSortHelper(array, start, right - 1)


print(quickSort([8, 9, 1, 0, -999, 1000, 90]))
