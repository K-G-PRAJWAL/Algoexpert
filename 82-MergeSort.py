# Solution 1
# def mergeSort(array):
#     '''
#     Time: O(nlog(n))
#     Space: O(nlog(n))
#     '''
#     if len(array) == 1:
#         return array
#     middle = len(array) // 2
#     left = array[:middle]
#     right = array[middle:]
#     return mergeSorted(mergeSort(left), mergeSort(right))


# def mergeSorted(left, right):
#     sortedArray = [None] * (len(left) + len(right))
#     k = i = j = 0
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             sortedArray[k] = left[i]
#             i += 1
#         else:
#             sortedArray[k] = right[j]
#             j += 1
#         k += 1
#     while i < len(left):
#         sortedArray[k] = left[i]
#         i += 1
#         k += 1
#     while j < len(right):
#         sortedArray[k] = right[j]
#         j += 1
#         k += 1
#     return sortedArray


# Solution 2
def mergeSort(array):
    if len(array) <= 1:
        return array
    aux = array[:]
    mergeSortHelper(array, 0, len(array) - 1, aux)
    return array


def mergeSortHelper(main, start, end, aux):
    if start == end:
        return
    middle = (start + end) // 2
    mergeSortHelper(aux, start, middle, main)
    mergeSortHelper(aux, middle + 1, end, main)
    doMerge(main, start, middle, end, aux)


def doMerge(main, start, middle, end, aux):
    k = start
    i = start
    j = middle + 1
    while i <= middle and j <= end:
        if aux[i] <= aux[j]:
            main[k] = aux[i]
            i += 1
        else:
            main[k] = aux[j]
            j += 1
        k += 1
    while i <= middle:
        main[k] = aux[i]
        i += 1
        k += 1
    while j <= end:
        main[k] = aux[j]
        j += 1
        k += 1


print(mergeSort([-133, 12, 0, -1, -99, 999, -10001]))
