class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def addChild(self, name):
        self.children.append(Node(name))

    def breadthFirstSearch(self, array):
        '''
        Time: O(V+E)
        Space: O(V)
        '''
        queue = [self]
        while len(queue) > 0:
            curr = queue.pop[0]
            array.append(curr.name)
            for child in curr.children:
                queue.append(child)
        return array
