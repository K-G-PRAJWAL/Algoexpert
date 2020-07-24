# Solution 1 - Iterative
# def PalindromeCheck(string):
#     '''
#     Time: O(n^2)
#     Space: O(n)
#     '''
#     new = ''
#     for i in reversed(range(len(string))):
#         new += string[i]
#     return new == string


# Solution 2 - Iterative
# def PalindromeCheck(string):
#     '''
#     Time: O(n)
#     Space: O(n)
#     '''
#     new = []
#     for i in reversed(range(len(string))):
#         new.append(string[i])
#     return ''.join(new) == string

# Solution 3 - Recursion
# def PalindromeCheck(string, i=0):
#     '''
#     Time: O(n)
#     Space: O(n)
#     '''
#     j = len(string) - 1 - i
#     return True if i >= j else string[i] == string[j] and PalindromeCheck(string, i+1)


# Solution 4 - Tail Recursion
# def PalidromeCheck(string, i=0):
#     '''
#     Time: O(n)
#     Space: O(n)
#     '''
#     j = len(string) - 1 - i
#     if i >= j:
#         return True
#     if string[i] != string[j]:
#         return False
#     return PalidromeCheck(string, i+1)


# Solution 5 - Pointers
def PalindromeCheck(string):
    '''
    Time: O(n)
    Space: O(1)
    '''
    left = 0
    right = len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True


print(PalindromeCheck("abcdcba"))
