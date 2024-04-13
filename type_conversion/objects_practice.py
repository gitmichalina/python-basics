# class Dog:
#     dogs_count = 0  # class attr
#
#     def __init__(self, name, age):
#         self.name = name  # obj attr
#         self.age = age  # obj attr
#         Dog.dogs_count += 1
#
#     def __del__(self):
#         Dog.dogs_count -= 1
#
#
# print(Dog.__dict__)
# burek = Dog("Burek", 36)
# print("")
# print(burek.__dict__)


# class ExampleClass:
#     my_class_attr = 0
#
#     def __init__(self, my_instance_attr):
#         self.my_instance_attr = my_instance_attr
#
#
# my_obj1 = ExampleClass(1)
# my_obj2 = ExampleClass(2)
#
# my_obj2.my_class_attr = 556
#
# print(my_obj1.__dict__)
# print(my_obj2.__dict__)
# print(ExampleClass.__dict__)
#
# ExampleClass.my_class_attr = 99
#
# print(my_obj1.__dict__)
# print(my_obj2.__dict__)
# print(ExampleClass.__dict__)
#
# print(my_obj1.my_class_attr)
# print(my_obj2.my_class_attr)
#

class ExampleClass:
    """
         This class is awsome.
    """
    my_class_attr = 666

    def __init__(self, my_instance_attr):
        self.my_instance_attr = my_instance_attr

    def my_instance_method(self):
        self.my_instance_attr += 1

    @staticmethod
    def my_static_method(arg1):
        pass

    @classmethod
    def my_class_method(cls, arg1):
        pass


m = ExampleClass(1)
print(hasattr(m, 'my_instance_attr'))
print(setattr(m, 'my_instance_attr', 3))
print(getattr(m, 'my_instance_attr'))
print(delattr(m, 'my_instance_attr'))
print(hasattr(m, 'my_instance_attr'))

n = dict()
print(n.values())