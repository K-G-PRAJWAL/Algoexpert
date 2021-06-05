# Solution 1
def smallestDifference(A, B):
    '''
    Time: O(nlog(n)+mlog(m)), n = length of A, m = length of B
    Space: O(1)
    '''
    A.sort()
    B.sort()
    i, j = 0, 0
    smallest = float("inf")
    curr = float("inf")
    pair = []
    while i < len(A) and j < len(B):
        first = A[i]
        second = B[j]
        if first < second:
            curr = second - first
            i += 1
        elif second < first:
            curr = first - second
            j += 1
        else:
            return [first, second]
        if smallest > curr:
            smallest = curr
            pair = [first, second]
    return pair


print(smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))
