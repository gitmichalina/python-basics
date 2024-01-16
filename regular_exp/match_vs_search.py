import re

a = ["this", "is", "to", "test"]
for s in a:
    x = re.match(r"(g\w+)\W(g\w+)", s)
    if x:
        print((x.groups()))

a = ["this", "is", "to", "test"]
s = "test"
for t in a:
    print('Found "%s" in "%s" -> ' % (t, s), end=" ")
    if re.search(t, s):
        print('found a match!')
    else:
        print('no match')

# Found "this" in "test" ->  no match
# Found "is" in "test" ->  no match
# Found "to" in "test" ->  no match
# Found "test" in "test" ->  found a match!