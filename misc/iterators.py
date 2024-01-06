it = iter([2, 3, 5])
print(next(it))
print(next(it))
print(next(it))
print(next(it))

def main():

    #for loop
    ls = MyList([1, 2, 3, 4])
    for e in ls:
        print(e)

    # alternatywa dla pętli for

    ls = MyList([1, 2, 3, 4])
    it = iter(ls)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break



class MyList:
    def __init__(self, ls):
        self.ls = ls

    def __iter__(self):
        return Reverser(self.ls)


class Reverser:
    def __init__(self, ls):
        self.ls = ls
        self.index = len(self.ls)

    def __next__(self):
        self.index = self.index - 1
        if self.index >= 0:
            return self.ls[self.index]
        raise StopIteration


