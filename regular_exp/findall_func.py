import re

# displays the non-alphanumeric characters.
x = re.compile(r'\W')
print(x.findall("This is costs rs100/0-"))
# [' ', ' ', ' ', '/', '-']

# extracts all the digits from the given string. The \d extracts all the digits.
x = re.compile(r'\d')
print(x.findall("we got independence on 15th august 1947"))
# ['1', '5', '1', '9', '4', '7']


my_str = "This is to test the regex test"
s = re.findall("test", my_str)
print(s)
# ['test', 'test']
