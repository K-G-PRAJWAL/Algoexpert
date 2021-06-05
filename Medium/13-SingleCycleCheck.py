def singleCycleCheck(array):
    '''
    Time: O(n)
    Space: O(1)
    '''
    visited = 0
    currIdx = 0
    while visited < len(array):
        if visited > 0 and currIdx == 0:
            return False
        visited += 1
        currIdx = nextIndex(currIdx, array)
    return currIdx == 0


def nextIndex(curr, array):
    next = (curr + array[curr]) % len(array)
    return next if next >= 0 else next+len(array)


print(singleCycleCheck([2, 3, 1, -4, -4, 2]))
