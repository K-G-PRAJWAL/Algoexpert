def moveElementToEnd(array, num):
    '''
    Time: O(n)
    Space: O(1)
    '''
    i = 0
    j = len(array) - 1
    while i < j:
        while array[j] == num and i < j:
            j -= 1
        if array[i] == num:
            array[i], array[j] = array[j], array[i]
        i += 1
    return array


print(moveElementToEnd([2, 1, 2, 2, 2, 3, 4, 2], 2))
