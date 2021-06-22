class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        # Input : Node
        # Output : array is the result
        # Add the current_node to the "array" and call 
        # depthFirstSearch for every child of this current_node.
        
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array
