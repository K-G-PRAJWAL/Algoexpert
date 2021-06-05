def productSum(array, multiplier=1):
    '''
    Time: O(n)
    Space: O(Depth of nested arrays)
    '''
    sum = 0
    for i in array:
        if type(i) is list:
            sum += productSum(i, multiplier + 1)
        else:
            sum += i
    return sum*multiplier


print(productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]))
