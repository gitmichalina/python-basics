from json import *
print(globals())


def foo(param1, param2):
    s = "local variable"
    print(locals())

# {'__name__': '__main__', '__doc__': None, '__package__': None,
# '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000002805DCABDA0>,
# '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>,
# '__file__': 'C:\\Users\\micha\\Projects\\PyCharm\\python-basics\\scopes_and_namespaces\\globals_and_import.py',
# '__cached__': None, 'dump': <function dump at 0x000002805E31C680>, 'dumps': <function dumps at 0x000002805E31C860>,
# 'load': <function load at 0x000002805E31D440>, 'loads': <function loads at 0x000002805E31D4E0>,
# 'JSONDecoder': <class 'json.decoder.JSONDecoder'>,
# 'JSONDecodeError': <class 'json.decoder.JSONDecodeError'>,
# 'JSONEncoder': <class 'json.encoder.JSONEncoder'>}

foo(1, 2)