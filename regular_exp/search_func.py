import re

txt = "It is still raining"
s = re.search(r"\s", txt)
print("First white-space at:", s.start())

# First white-space at: 2

my_str = "This is to test"
s = re.search("test", my_str)
print(s.span())
print(s.group())
print(s.string)

# (11, 15)
# test
# This is to test

my_str = "This is to test the regex test"
s = re.search("test", my_str)
print(s)
print(type(s))

# <re.Match object; span=(11, 15), match='test'>
# <class 're.Match'>
