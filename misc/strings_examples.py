from math import pi

print(f'Area is {365656565656565336*7/3:9.3f}.')

# f'{"abc":6}' daje 'abc '
# f'{"abc":>6}' daje ' abc'
# f'{123:6d}' daje ' 123'
# f'{123:<6d}' daje '123 '
# f'{pi:6.2f}' daje '3.14'
# f'{pi:<6.2f}' daje '3.14 '


print('pi is {:8.4f}'.format(pi))

print('pi is {:8.4f}'.format(1521512))

formatted = "{1} {0} {1}".format(1, 2, 3, 4)
print(formatted)

my_string = "%s = %i" % ('x', 7)
print(my_string)
