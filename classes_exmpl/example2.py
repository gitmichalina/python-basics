class MyClass:

    def __init__(self, value):
        self.__private_value = value

    def __my_private_method(self):
        return '__mymethod__ called'

    def my_instance_method(self):
        return 'my_instance_method called'

    # def static_method(self):
    #     return 'instance method called', self
    #
    # @classmethod
    # def classmethod(cls):
    #     return 'class method called', cls
    #
    # @staticmethod
    # def staticmethod():
    #     return 'static method called'

    # def __mymethod(self):
    #     return '__instance method called'


my_object = MyClass(10)
# print(my_object.__private_value)
# print(my_object.__my_private_method())

# print(my_object._MyClass__private_value)
# print(my_object._MyClass__my_private_method())

# my_object = MyClass("name")
# print(my_object.static_method())
#
# print(MyClass.classmethod())
# print(MyClass.staticmethod())
#
# my_object._MyClass__value = "plpl"
# print(my_object._MyClass__mymethod())
#
# print(my_object._MyClass__value)

# print(my_object.__dict__.items())
# # dict_items([('_MyClass__private_value', 10)])
#
# print(MyClass.__dict__)

print(vars(my_object))
print(vars(MyClass))
my_object.__dict__['__value'] = 67
print(vars(my_object))


# {'__module__': '__main__',
# '__init__': <function MyClass.__init__ at 0x0000024416FA4D60>,
# '_MyClass__my_private_method': <function MyClass.__my_private_method at 0x0000024416FA63E0>,
# 'my_instance_method': <function MyClass.my_instance_method at 0x0000024416FA5A80>,
# '__dict__': <attribute '__dict__' of 'MyClass' objects>,
# '__weakref__': <attribute
# '__weakref__' of 'MyClass' objects>,
# '__doc__': None}


# class MySampleClass:
#     my_cls_attr = 100
#
#     def __init__(self, inst_attr):
#         self.inst_attr = inst_attr
#
#     def method(self):
#         print(f"Class attribute: {self.my_cls_attr}")
#         print(f"Instance attribute: {self.inst_attr}")
#
#
# print(MySampleClass.__dict__)
