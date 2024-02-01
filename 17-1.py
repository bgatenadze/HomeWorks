#1.	შექმენი კლასი რომელსაც ექნება public, protected და private პარამეტრები.
# გამოიყენე @property დეკორატორი და ასევე შექმენი setter და  getter დეკორატორებიანი ფუნქციები
# პარამეტრებზე წვდომისა და რედაქტირებისთვის.    

class ExampleClass:
    def __init__(self, public_param, protected_param, private_param):
        self.public_param = public_param
        self._protected_param = protected_param
        self.__private_param = private_param

    # Getter method for public_param
    @property
    def public_param(self):
        return self._public_param

    # Setter method for public_param
    @public_param.setter
    def public_param(self, value):
        self._public_param = value

    # Getter method for protected_param
    @property
    def protected_param(self):
        return self._protected_param

    # Setter method for protected_param
    @protected_param.setter
    def protected_param(self, value):
        self._protected_param = value

    # Getter method for private_param
    @property
    def private_param(self):
        return self.__private_param

    # Setter method for private_param
    @private_param.setter
    def private_param(self, value):
        self.__private_param = value

# Example usage:
example_instance = ExampleClass(public_param=1, protected_param=2, private_param=3)

# Accessing public_param (using the getter method)
print(example_instance.public_param)  # Output: 1

# Modifying public_param (using the setter method)
example_instance.public_param = 42

# Accessing protected_param (using the getter method)
print(example_instance.protected_param)  # Output: 2

# Modifying protected_param (using the setter method)
example_instance.protected_param = 99

# Accessing private_param (using the getter method)
print(example_instance.private_param)  # Output: 3

# Modifying private_param (using the setter method)
example_instance.private_param = 100

# Accessing private_param again to verify the change
print(example_instance.private_param)  # Output: 100