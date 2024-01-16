from os import *
x = "some value"


def some_function():
    pass


class SomeClass():
    ...


print(type(globals()))
# <class 'dict'>

print(globals()['x'])
# some value

globals()['x'] = 4.33
print(globals()['x'])
# 4.33 because of reassignment

print(x is globals()['x'])
# True

print(globals())
# {'name': 'main', 'doc': None, 'package': None,
# 'loader': <_frozen_importlib_external.SourceFileLoader object at 0x000001D1D9F9BDA0>, 'spec': None,
# 'annotations': {}, 'builtins': <module 'builtins' (built-in)>,
# 'file': 'C:\\Users\\micha\\Projects\\PyCharm\\python-basics\\scopes_and_namespaces\\aa_global.py',
# 'cached': None, 'x': 4.33, 'some_function': <function some_function at 0x000001D1D9F8A2A0>,
# 'SomeClass': <class 'main.SomeClass'>}


