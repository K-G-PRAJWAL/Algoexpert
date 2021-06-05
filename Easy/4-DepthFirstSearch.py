class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))

    def depthFirstSearch(self, array):
        '''
        Time: O(Vertices+Edges)
        Space: O(Vertices)
        '''
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array
