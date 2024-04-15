# tree.py

class TreeNode:
    def __init__(self, data):
        self._data = data
        self._children = []

    @property
    def children(self):
        return self._children

    @children.setter
    def children(self, value):
        if isinstance(value, list):
            self._children = value
        else:
            del self.children
            self._children.append(value)

    @children.deleter
    def children(self):
        self._children.clear()

    def __repr__(self):
        return f'{self.__class__.__name__}("{self._data}")'


root = TreeNode("root")
child1 = TreeNode("child 1")
child2 = TreeNode("child 2")

root.children = [child1, child2]
print(root.children)
del root.children
print(root.children)
