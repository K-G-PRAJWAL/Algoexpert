# Solution 1
# def groupAnagrams(words):
#     '''
#     Time: O(W.N.log(N))
#     Space: O(W.N)
#     '''
#     if len(words) == 0:
#         return []
#     sortedWords = ["".join(sorted(word)) for word in words]
#     indices = [i for i in range(len(words))]
#     indices.sort(key=lambda x: sortedWords[x])
#     result = []
#     currAnagramGroup = []
#     currAnagram = sortedWords[indices[0]]
#     for index in indices:
#         word = words[index]
#         sortedWord = sortedWords[index]
#         if sortedWord == currAnagram:
#             currAnagramGroup.append(word)
#             continue
#         result.append(currAnagramGroup)
#         currAnagramGroup = [word]
#         currAnagram = sortedWord
#     result.append(currAnagramGroup)
#     return result


# Solution 2
def groupAnagrams(words):
    '''
    Time: O(W.N.log(N))
    Space: O(W.N)
    '''
    anagrams = {}
    for word in words:
        sortedWord = "".join(sorted(word))
        if sortedWord in anagrams:
            anagrams[sortedWord].append(word)
        else:
            anagrams[sortedWord] = [word]
    return list(anagrams.values())


print(groupAnagrams(['yo', 'act', 'flop', 'tac', 'cat', 'oy', 'olfp']))
