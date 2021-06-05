class MinMaxStack:
    def __init__(self):
        self.minmaxStack = []
        self.stack = []

    def peek(self):
        '''
        Time: O(1)
        Space: O(1)
        '''
        return self.stack[len(self.stack)-1]

    def push(self, num):
        '''
        Time: O(1)
        Space: O(1)
        '''
        newMinMax = {'min': num, "max": num}
        if len(self.minmaxStack):
            lastMinMax = self.minmaxStack[len(self.minmaxStack) - 1]
            newMinMax["min"] = min(lastMinMax["min"], num)
            newMinMax["max"] = max(lastMinMax["max"], num)
        self.minmaxStack.append(newMinMax)
        self.stack.append(num)

    def pop(self):
        '''
        Time: O(1)
        Space: O(1)
        '''
        self.minmaxStack.pop()
        return self.stack.pop()

    def getMin(self):
        '''
        Time: O(1)
        Space: O(1)
        '''
        return self.minmaxStack[len(self.minmaxStack)-1]["min"]

    def getMax(self):
        '''
        Time: O(1)
        Space: O(1)
        '''
        return self.minmaxStack[len(self.minmaxStack)-1]["max"]


obj = MinMaxStack()
obj.push(5)
obj.push(2)
obj.push(1)
obj.push(11)
obj.push(7)
obj.pop()
obj.push(3)
print(obj.peek())
print(obj.getMax())
print(obj.getMin())
