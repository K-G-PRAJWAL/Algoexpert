def TwoNumberSum(arr, target):
    # Solution 1 - O(n) time | O(n) space
    dictionary = {}
    for i in range(len(arr) - 1):
        a = arr[i]
        b = target - a
        if b in dictionary:
            return [b, a]
        else:
            dictionary[a] = b
    return []

    # Solution 2 - O(n^2) time | O(1) space
    # for i in range(len(arr)-1):
    #     a = arr[i]
    #     for j in range(i+1, len(arr)-1):
    #         b = arr[j]
    #         if a+b == target:
    #             return [a, b]
    # return []

    # Solution 3 - O(n log n) time | O(1) space
    # arr.sort()
    # l = 0
    # r = len(arr)-1
    # while l < r:
    #     sum = arr[l] + arr[r]
    #     if sum == target:
    #         return [arr[l], arr[r]]
    #     elif sum < target:
    #         l += 1
    #     elif sum > target:
    #         r += 1
    # return []


ans = TwoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10)
print(ans)
