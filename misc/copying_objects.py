# import copy
import copy as deep_copy


# SHALLOW COPY

grades = [["Marta", "5+"], ["Misia", "4"]]
grades2 = grades[:]          # new list containing copies of those references
grades2[0] = ["Gaston", "3"] # first reference has changed, new list on index 0 now
grades2[1][1] = "2"          # gardes[1] and grades2[1] both refer to the same list. And list has changed!
print(grades) # [['Marta', '5+'], ['Misia', '2']]
print(grades2) # [['Gaston', '3'], ['Misia', '2']]
# DEEP COPY

grades3 = deep_copy.deepcopy(grades)
grades3[1][1] = "1"
# grades is unchanged
print(grades) # [['Marta', '5+'], ['Misia', '2']]
print(grades2) # [['Gaston', '3'], ['Misia', '2']]
print(grades3)

for _ in range(0, 3):
    print("Hello!")