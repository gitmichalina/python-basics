import re

s = 'five:5 twenty one:21 ten:10'
p = r'\d+'
r = re.split(p, s, 1)
print(r)

