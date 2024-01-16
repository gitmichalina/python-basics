class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'

my_object = MyClass()
print(my_object.method())

print(MyClass.classmethod())
print(MyClass.staticmethod())