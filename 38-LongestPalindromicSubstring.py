def longestPalindromicSubstring(s):
    '''
    Time: O(n^2)
    Space: O(1)
    '''
    currLongest = [0, 1]
    for i in range(1, len(s)):
        odd = getLongestPalindrome(s, i - 1, i + 1)
        even = getLongestPalindrome(s, i - 1, i)
        longest = max(odd, even, key=lambda x: x[1] - x[0])
        currLongest = max(longest, currLongest, key=lambda x: x[1] - x[0])
    return s[currLongest[0]:currLongest[1]]


def getLongestPalindrome(string, l, r):
    while l >= 0 and r < len(string):
        if string[l] != string[r]:
            break
        l -= 1
        r += 1
    return [l+1, r]


print(longestPalindromicSubstring('abcabbaba'))
