# binding with immutable
a = 5           # bind a to 5
b = a           # copy a's binding into b
a = 6           # change the binding of a
print(b)        # b is still bound to 5

# binding with mutable
a = [1, 2, 3]   # bind a to the list
b = a           # copy a's binding into b
a[0] = 99       # change the list, not the bindings
print(b)        # b still bound to the same list,
                # but the list is now [99, 2, 3]

def foo(a, b):
    a[0] = 99
    b = [7, 8]

a = [1, 2, 3]
b = [1, 2, 3]

foo(a, b)
print(a, b) # [99, 2, 3] [1, 2, 3]