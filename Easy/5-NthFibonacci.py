def getNthFib(n):
    # Solution 1
    '''
    Time: O(2^n)
    Space: O(n)
    '''
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return getNthFib(n - 1) + getNthFib(n - 2)


def getNthFib(n, memoize={1: 0, 2: 1}):
    # Solution 2
    '''
    Time: O(n)
    Space: O(n)
    '''
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = getNthFib(n - 1, memoize) + getNthFib(n - 2, memoize)
        return memoize[n]


def getNthFib(n):
    # Solution 3
    '''
    Time: O(n)
    Space: O(1)
    '''
    last = [0, 1]
    counter = 3
    while counter <= n:
        next = last[0] + last[1]
        last[0] = last[1]
        last[1] = next
        counter += 1
    return last[1] if n > 1 else last[0]


print(getNthFib(6))
