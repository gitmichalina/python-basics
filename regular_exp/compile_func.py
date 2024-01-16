import re

# displays alphanumeric group characters.
x = re.compile(r'\w+')
print(x.findall("This pen costs rs100/-"))
# ['This', 'pen', 'costs', 'rs100']

# extracts the digits from the given string
x = re.compile(r'\d')
print(x.findall("this is my 1st experiment on regex"))
# ['1']