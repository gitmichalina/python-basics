# stack.py

class Stack:
    def __init__(self, items=None):
        if items is None:
            self._items = []
        else:
            self._items = list(items)

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self._items})"


my_stack = Stack([1, 2, 3])
print(my_stack)
my_stack.push(4)
print(my_stack)
my_stack.pop()
print(my_stack)

# Stack([1, 2, 3])
# Stack([1, 2, 3, 4])
# Stack([1, 2, 3])

print(dir(my_stack))


# ['__class__', '__delattr__', '__dict__', ....
# '_items', 'pop', 'push']


class StackList(list):
    def push(self, item):
        self.append(item)

    def pop(self):
        return super().pop()

    def __repr__(self) -> str:
        return f"{type(self).__name__}({super().__repr__()})"


stackList = StackList()
print(dir(stackList))
# ['__add__', '__class__', ..... 'append',
# 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'push',
# 'remove', 'reverse', 'sort']
