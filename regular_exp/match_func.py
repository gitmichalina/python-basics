import re

s = "this is to test the python regular expressions"
m = re.match(r'(.*)are(.*?).*', s, re.M)
print(m)
if m:
    print(m.group())
    print(m.group(1))
    print(m.group(2))

# None

# searches whether any word starts with ‘t’ and word length is four.
s = "this is to test"
x = re.match("^t...", s)
if x:
    print("found")
else:
    print("not found")

# found
