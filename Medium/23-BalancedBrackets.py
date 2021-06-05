def balancedBrackets(s):
    '''
    Time: O(N)
    Space: O(N)
    '''
    stack = []
    for i in s:
        if i == '[' or i == '(' or i == '{':
            stack.append(i)
        elif i == ')' and len(stack) and stack[-1] == '(':
            stack.pop()
        elif i == ']' and len(stack) and stack[-1] == '[':
            stack.pop()
        elif i == '}' and len(stack) and stack[-1] == '{':
            stack.pop()
    return len(stack) == 0


print(balancedBrackets('(([]()()){})'))
