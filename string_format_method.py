s = "{}{}{}{}".format('this', 'is', 'for', 'test')
print(s)
# thisisfortest
s = "{} {} {} {}".format('this', 'is', 'for', 'test')
print(s)
# this is for test
s = "{3}{2}{1}{0}".format('this', 'is', 'for', 'test')
print(s)
# testforisthis

s = "{t}{i}{f}{e}".format(t='this', i='is', f='for', e='test')
print(s)
# thisisfortest

s = "{}, string format example".format("pyhton")
print(s)
# pyhton, string format example

s = "string example in {}".format("pyhton")
print(s)
# string example in pyhton
