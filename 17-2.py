#2.	შექმენი მისი შვილობილი კლასი და შეუცვალე რაიმე არსებული მეთოდი.

class ExampleClass:
    def __init__(self, public_param, protected_param, private_param):
        self.public_param = public_param
        self._protected_param = protected_param
        self.__private_param = private_param

    @property
    def public_param(self):
        return self._public_param

    @public_param.setter
    def public_param(self, value):
        self._public_param = value

    @property
    def protected_param(self):
        return self._protected_param

    @protected_param.setter
    def protected_param(self, value):
        self._protected_param = value

    @property
    def private_param(self):
        return self.__private_param

    @private_param.setter
    def private_param(self, value):
        self.__private_param = value

class ChildClass(ExampleClass):
    def __init__(self, public_param, protected_param, private_param, additional_param):
        super().__init__(public_param, protected_param, private_param)
        self.additional_param = additional_param

    @property
    def protected_param(self):
        return self._protected_param

    @protected_param.setter
    def protected_param(self, value):
        super(ChildClass, ChildClass).protected_param.__set__(self, value * 2)

# Example usage of the child class:
child_instance = ChildClass(public_param=10, protected_param=20, private_param=30, additional_param=40)

print(child_instance.public_param)       # Output: 10
print(child_instance.protected_param)    # Output: 40 (because the setter method in the child class modified it)

child_instance.public_param = 100
child_instance.protected_param = 200

print(child_instance.private_param)      # Output: 30
print(child_instance.additional_param)   # Output: 40
