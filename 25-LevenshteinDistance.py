# Solution 1
# def levenshteinDistance(str1, str2):
#     '''
#     Time: O(NM)
#     Space: O(NM)
#     '''
#     arr = [[x for x in range(len(str1)+1)] for y in range(len(str2)+1)]
#     for i in range(1, len(str2) + 1):
#         arr[i][0] = arr[i-1][0]+1
#     for i in range(1, len(str2) + 1):
#         for j in range(1, len(str1) + 1):
#             if str2[i - 1] == str1[j - 1]:
#                 arr[i][j] = arr[i - 1][j - 1]
#             else:
#                 arr[i][j] = 1 + min(arr[i - 1][j], arr[i]
#                                     [j - 1], arr[i - 1][j - 1])
#     return arr[-1][-1]

# Soluton 2
def levenshteinDistance(str1, str2):
    '''
    Time: O(NM)
    Space: O(min(N, M))
    '''
    small = str1 if len(str1) < len(str2) else str2
    big = str1 if len(str1) >= len(str2) else str2
    arr = [[x for x in range(len(str1) + 1)] for y in range(len(str2) + 1)]
    evenArr = [x for x in range(len(small)+1)]
    oddArr = [None for x in range(len(small) + 1)]
    for i in range(1, len(big) + 1):
        if i % 2 == 1:
            currArr = oddArr
            prevArr = evenArr
        else:
            currArr = evenArr
            prevArr = oddArr
        currArr[0] = i
        for j in range(1, len(small) + 1):
            if big[i - 1] == small[j - 1]:
                currArr[j] = prevArr[j - 1]
            else:
                currArr[j] = 1 + min(prevArr[j - 1],
                                     prevArr[j], currArr[j - 1])
    return evenArr[-1] if len(big) % 2 == 0 else oddArr[-1]


print(levenshteinDistance("abc", "yabd"))
