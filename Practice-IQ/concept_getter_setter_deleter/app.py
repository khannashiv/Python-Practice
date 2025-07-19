## Simple example of getter, setter & deleter in python.

class person():
    def __init__(self, name, age):
        self._name = name   # private attribute / private data members / private variable
        self._age = age     # same as above
    
    # Getter for name attribute.
    @property
    def name(self):
        return self._name
    
    # Setter for name attribute.
    @name.setter
    def name(self, value):
        if len(value) > 1:
            self._name=value
        else:
            raise ValueError("Name must has atleast 2 characters.")

    # Getter for age attribute.
    @property
    def age(self):
        return self._age
    
    # Setter for age attribute.
    @age.setter
    def age(self, value):
        if value >=0:
            self._age = value
        else:
            raise ValueError("Age cannot be -ve.")
        

    # Deleter for name attribute.
    @name.deleter
    def name(self):
        print("Deleting name...")
        del self._name  # Deleting the actual internal attribute # Test this part by commenting out during revision.

    # Deleter for age attribute.
    @age.deleter
    def age(self):
        print("Deleting age...")
        del self._age  # Deleting the actual internal attribute

# Creating an object of class.

person = person("Shiv", 30)

# Accessing the properties via getters

print(person.age)
print(person.name)

# Modifying the properties via setters

person.name = "Bob"
person.age = 20

# Accessing the properties again after modifying the values via setter.

print(person.name)
print(person.age)

# Deleting the properties via deleters.

del person.name # Deleting the name property.
del person.age  # Deleting the age property.

# Checking the object after deletion
print(person.__dict__) 