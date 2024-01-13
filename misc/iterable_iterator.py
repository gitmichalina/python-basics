class MyIterableList:
    def __init__(self, a_list):
        self.a_list = a_list

    def __iter__(self):
        return IteratorReverser(self.a_list)


class IteratorReverser:
    def __init__(self, a_list):
        self.a_list = a_list
        self.index = len(self.a_list)

    def __next__(self):
        self.index = self.index - 1
        if self.index >= 0:
            return self.a_list[self.index]
        raise StopIteration


my_list = MyIterableList([1, 2, 3, 4])
for e in my_list:
    print(e)

my_list = MyIterableList([1, 2, 3, 4])
my_iterator = iter(my_list)
while True:
    try:
        print(next(my_iterator))
    except StopIteration:
        break
