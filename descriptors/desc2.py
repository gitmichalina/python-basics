# property_decorator.py
class TestClass():
    @property
    def test_attribute(self) -> object:
        print("accessing the attribute to get the value")
        return 42

    @test_attribute.setter
    def test_attribute(self, value) -> None:
        print("accessing the attribute to set the value")
        raise AttributeError("Cannot change the value")


test_object = TestClass()
print(test_object.test_attribute)
test_object.test_attribute = 9
