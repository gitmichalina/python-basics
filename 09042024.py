a = [1,3,4]
print(id(a))
b = a[:]
print(b)
print(id(b))

eng2sp = {"one": "uno", "two": "dos", "three": "tres"}
print(type(eng2sp.values()))
print(eng2sp.values())
vals = list(eng2sp.values())

