# Solution 1
# def caesarCipher(string, key):
#     '''
#     Time: O(n)
#     Space: O(n)
#     '''
#     ans = ''
#     for letter in string:
#         asci = ord(letter)
#         encrypt = asci + (key % 26)
#         if encrypt <= 122:
#             ans += chr(encrypt)
#         else:
#             ans += chr(96 + (encrypt % 122))
#     return ans

# Solution 2
# def caesarCipherEncryptor(string, key):
#     '''
#     Time: O(n)
#     Space: O(n)
#     '''
#     new = []
#     key = key % 26
#     for letter in string:
#         new.append(getLetter(letter, key))
#     return "".join(new)


# def getLetter(letter, key):
#     newCode = ord(letter) + key
#     return chr(newCode) if newCode <= 122 else chr(96+newCode % 122)


# Solution 3
def caesarCipherEncryptor(string, key):
    '''
    Time: O(n)
    Space: O(n)
    '''
    new = []
    key = key % 26
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    for letter in string:
        new.append(getLetter(letter, key, alphabet))
    return "".join(new)


def getLetter(letter, key, alphabet):
    newCode = alphabet.index(letter) + key
    return alphabet[newCode] if newCode <= 25 else alphabet[-1+newCode % 25]


print(caesarCipherEncryptor('xyz', 54))
