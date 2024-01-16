import re

print(re.escape("this is to test"))
print(re.escape("this is to test \t ^test"))

# this\ is\ to\ test
# this\ is\ to\ test\ \	\ \^test