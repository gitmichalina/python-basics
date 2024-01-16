def foo(param1, param2):
    s = "local variable"
    print(locals())


foo(1, 2)
# {'param1': 1, 'param2': 2, 's': 'local variable'}