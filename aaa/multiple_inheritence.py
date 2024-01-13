class MotherClass:
    def mother_method(self):
        print('mother_method')

    def same_name_method(self):
        print('same name method in mother class')


class FatherClass:
    def father_method(self):
        print('father_method')

    def same_name_method(self):
        print('same name method in father class')


class ChildClass(MotherClass, FatherClass):
    def child_method(self):
        print('child_method')


child_object = ChildClass()
child_object.mother_method()
child_object.father_method()
child_object.child_method()
child_object.same_name_method()
print(ChildClass.mro())