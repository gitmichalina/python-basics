import copy



# SHALLOW COPY

grades = [["Marta", "5+"], ["Misia", "4"]]
grades2 = grades[:]
grades2[0] = ["Gaston", "3"]
grades2[1][1] = "2"
print(grades) # [['Marta', '5+'], ['Misia', '2']]
print(grades2) # [['Gaston', '3'], ['Misia', '2']]

# DEEP COPY

grades3 = copy.deepcopy(grades)
grades3[1][1] = "1"
# grades is unchanged
print(grades) # [['Marta', '5+'], ['Misia', '2']]
print(grades2) # [['Gaston', '3'], ['Misia', '2']]
print(grades3)

for _ in range(0, 3):
    print("Hello!")