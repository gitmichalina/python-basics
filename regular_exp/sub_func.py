import re

s = 'this is to test'
p = r'\s+'
r = 'X'
s1 = re.sub(p, r, s)
print(s1)

# thisXisXtoXtest