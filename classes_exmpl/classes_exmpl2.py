# class Person(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def say_hi(self):
#         print('Hello', self.name)
#
#
# class ExampleClass():
#     def __new__(cls):
#         print("creating object")
#
#     def __init__(self):
#         print("initialisation")
#
# class NewExampleClass():
#     def __new__(cls):
#         print("creating object")
#         return super(NewExampleClass, cls).__new__(cls)
#
#     def __init__(self):
#         print("initialisation")
#
#
# NewExampleClass()


class MyClass():

    class_var = 1

    def instance_method(self):
        print("instance method")

    @classmethod
    def class_method(cls):
        print("class method")

    @staticmethod
    def static_method():
        print("static method")


example_object = MyClass()

example_object.instance_method()
example_object.class_method()
MyClass.class_method()

MyClass.static_method()
example_object.static_method()

MyClass.class_var = 4
print(MyClass.class_var)


