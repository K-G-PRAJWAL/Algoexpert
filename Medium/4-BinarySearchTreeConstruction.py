class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        '''
        Insert an element into the BST
        Average time: O(log(n)) | Average Space: O(1)
        Worst time: O(n) | Worst Space: O(1)
        '''
        curr = self
        while True:
            if value < curr.value:
                if curr.left is None:
                    curr.left = BST(value)
                    break
                else:
                    curr = curr.left
            else:
                if curr.right is None:
                    curr.right = BST(value)
                    break
                else:
                    curr = curr.right
        return self

    def contains(self, value):
        '''
        Search for an element in the BST
        Average time: O(log(n)) | Average Space: O(1)
        Worst time: O(n) | Worst Space: O(1)
        '''
        curr = self
        while curr is not None:
            if value < curr.value:
                curr = curr.left
            elif value > curr.right:
                curr = curr.right
            else:
                return True
        return False

    def remove(self, value, parentNode=None):
        '''
        Remove an element from the BST
        Average time: O(log(n)) | Average Space: O(1)
        Worst time: O(n) | Worst Space: O(1)
        '''
        curr = self
        while curr is not None:
            if value < curr.value:
                parentNode = curr
                curr = curr.left
            elif value > curr.value:
                parentNode = curr
                curr = curr.right
            else:
                if curr.left is not None and curr.right is not None:
                    curr.value = curr.right.getMinValue()
                    curr.right.remove(curr.value, curr)
                elif parentNode is None:
                    if curr.left is not None:
                        curr.value = curr.left.value
                        curr.right = curr.left.right
                        curr.left = curr.left.left
                    elif curr.right is not None:
                        curr.value = curr.right.value
                        curr.left = curr.right.left
                        curr.right = curr.right.right
                    else:
                        curr.value = None
                elif parentNode.left == curr:
                    parentNode.left = curr.left if curr.left is not None else curr.right
                elif parentNode.right == curr:
                    parentNode.right = curr.left if curr.left is not None else curr.right
                break
        return self


def getMinValue(self):
    curr = self
    while curr.left is not None:
        curr = curr.left
    return curr.value
