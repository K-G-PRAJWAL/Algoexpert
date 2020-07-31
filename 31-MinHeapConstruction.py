class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        '''
        Time: O(N)
        Space: O(1)
        '''
        firstParentIdx = (len(array) - 2) // 2
        for currIdx in reversed(range(firstParentIdx)):
            self.siftDown(currIdx, len(array)-1, array)

    def siftDown(self, currIdx, endIdx, heap):
        '''
        Time: O(log(N))
        Space: O(1)
        '''
        child1Idx = currIdx * 2 + 1
        while child1Idx <= endIdx:
            child2Idx = currIdx * 2 + 2 if currIdx * 2 + 2 <= endIdx else - 1
            if child2Idx != -1 and heap[child2Idx] <= heap[child1Idx]:
                idxToSwap = child2Idx
            else:
                idxToSwap = child1Idx
            if heap[idxToSwap] < heap[currIdx]:
                self.swap(currIdx, idxToSwap, heap)
                currIdx = idxToSwap
                child1Idx = currIdx * 2 + 1
            else:
                break

    def siftUp(self, currIdx, heap):
        '''
        Time: O(log(N))
        Space: O(1)
        '''
        parentIdx = (currIdx - 1) // 2
        while currIdx > 0 and heap[currIdx] < heap[parentIdx]:
            self.swap(currIdx, parentIdx, heap)
            currIdx = parentIdx
            parentIdx = (currIdx - 1)//2

    def peek(self):
        return self.heap[0]

    def remove(self):
        swap(0, len(self.heap) - 1, self.heap)
        valueToRemove = self.heap.pop()
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return valueToRemove

    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap)-1, self.heap)

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]
