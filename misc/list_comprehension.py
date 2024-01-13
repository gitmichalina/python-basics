


# [expression for variable in collection] is a new list formed by binding each value in the collection in turn to the variable,
# then evaluating the expression.

# doing something on every element in the list
new_list = [2 * x for x in [1, 2, 3]]
# new_list = [2, 4, 6]

# removing unwanted elements from the list by creating new list
new_list_2 = [x for x in [1, 0, 2] if x > 0]
# new_list_2 = [1, 2]