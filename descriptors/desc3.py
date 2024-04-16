# property_function.py
class TestClass():
    def getter(self) -> object:
        print("accessing the attribute to get the value")
        return 42

    def setter(self, value) -> None:
        print("accessing the attribute to set the value")
        raise AttributeError("Cannot change the value")

    test_attribute = property(getter, setter)


test_object = TestClass()
print(test_object.test_attribute)
