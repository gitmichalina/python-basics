my_list = [1, 2, 3]

def foo():
    # my_list = [5, 6] ok, as a new local variable
    my_list[1] = ["koko"]
    print(my_list)


foo()
# [1, ['koko'], 3]
print(my_list)
# [1, ['koko'], 3]