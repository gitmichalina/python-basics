from math import pi

print(f'Area is {365656565656565336 * 7 / 3:9.3f}.')

print(f'{"abc":6}')
# 'abc   '
print(f'{"abc":>6}')
# '   abc'
print(f'{123:6d}')
# '   123'
print(f'{123:<6d}')
# '123   '
print(f'{pi:6.2f}')
# '  3.14'
print(f'{pi:<6.2f}')
# '3.14  '


print('pi is {:8.4f}'.format(1521512))

formatted = "{1} {0} {1}".format(1, 2, 3, 4)
print(formatted)

my_string = "%s = %i" % ('x', 7)
print(my_string)

print(f'Area is {5 * 7 / 2:14.3f}.')

print('pi is {:8.4f}'.format(pi))

print('{1} {0} {1}'.format(5, 8, 9, 1))

print('%s = %i' % ('x', 7))