# descriptors.py
class Special_attribute():
    def __get__(self, obj, type=None) -> object:
        print("accessing the attribute to get the value")
        return 42

    def __set__(self, obj, value) -> None:
        print("accessing the attribute to set the value")
        raise AttributeError("Cannot change the value")


class TestClass():
    test_attribute = Special_attribute()


test_object = TestClass()
print(test_object.test_attribute)
test_object.test_attribute = 2


