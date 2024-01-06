


# [expression for variable in collection] is a new list
# formed by binding each value in the collection in turn to
# the variable, then evaluating the expression.

# zrobienie czegoś na każdym elemencie listy:
new_list = [2 * x for x in [1, 2, 3]] # returns [2, 4, 6]

# usunięcie niechcianych elementów z listy
new_list = [x for x in [1, 0, 2] if x > 0] # returns [1, 2].