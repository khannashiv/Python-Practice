## Different names or terms we use to refer to variables based on their context in Python.

    # Data member = instance variable = object variable = Attribute of an object in OOP
    # Member functions = Methods in OOP = Functions defined inside a class

# 1. Variables (General term)

    # Definition: The most generic term for any named reference to a value stored in memory.
    # Context: A variable can be used to store any kind of data (strings, numbers, lists, objects, etc.).
    # Example:

x = 10          # 'x' is a variable
name = "Shiv"  # 'name' is a variable

# 2. Data Members (or Attributes)

    # Definition: These are variables that are associated with a class (i.e., belong to an object or instance of the class). 
    # Data members hold data specific to that class instance.
    # Context: In object-oriented programming (OOP), data members refer to the variables that are tied to the state of an object.
    # They are often called attributes as well.
    # self.name and self.age are data members (or instance variables).
    # name and age on the right-hand side are just parameters passed to the __init__ method.
    # However, self is used inside the class to refer to the current object. 
    # You do not need to explicitly write self when accessing data members outside the class.

class Person:
    def __init__(self, name, age):
        self.name = name        # 'name' is a data member (attribute) / # Instance( object ) variable
        self.age = age          # 'age' is a data member (attribute) /  # Instance( object ) variable

person1 = Person("Shiv", 30)
print(person1.name)             # Accessing a data member

# Ques: How self works inside the class ?
# Sol : 
class Person:
    def __init__(self, name, age):
        self.name = name                # Instance variable (data member)
        self.age = age                  # Instance variable (data member)

    def print_name(self):
        print(f"My name is: {self.name.upper()}")  # Accessing the instance variable inside the class

person1 = Person("Shiv", 30)
person1.print_name()                        # Prints " My name is SHIV"

# 3. Arguments

    # Definition: Arguments are the values you pass into a function or method when calling it. 
    # These values are used by the function/method during execution.
    # Context: Arguments are used when calling functions or methods. 
    # They provide the actual input that the function operates on.

def greet(name): 
    print(f"Hello, {name}!")

greet("Shiv")  # "Shiv" is an argument

# 4. Parameters

    # Definition: Parameters are the variables listed in the function definition. 
    # They act as placeholders for the values (arguments) that will be passed to the function when it is called.
    # Context: Parameters are used in function/method definitions to define what values the function expects when it is called.

def greet(name):  # 'name' is a parameter
    print(f"Hello, {name}!")

greet("Shiv")  # "Shiv" is an argument

# 5. Local Variables

    # Definition: These are variables that are defined within a function or method.
    #  They exist only within the scope of that function and are local to it.
    # Context: Local variables are created when the function is called and are destroyed when the function execution is complete.

def add(x, y):      # 'x' and 'y' are parameters (local variables)
    result = x + y  # 'result' is a local variable
    return result

sum = add(3, 4)     # 'sum' is a variable that holds the return value
print(sum)

# 6. Instance Variables

    # Definition: These are variables that are bound to an instance of a class. 
    # They are usually initialized inside the __init__ constructor and can have different values for each instance of the class.
    # Context: These variables are typically referred to as data members (or attributes) 
    # but emphasize their link to a specific instance of a class.

class Car:
    def __init__(self, make, model):
        self.make = make               # 'make' is an instance variable
        self.model = model             # 'model' is an instance variable

car1 = Car("Toyota", "Corolla")
print(car1.make)                       # Accessing an instance variable

################ Test-1 ########################

# self.var_1 and self.var_2 are instance variables (or data members) of the Car class.
# make and model are parameters in the __init__ method.They are just placeholders that receive values when an object of the class is created.
# These parameters are used to initialize the data members (instance variables).
# 
class Car:
    def __init__(self, make, model):
        self.var_1 = make              
        self.var_2 = model           

car1 = Car("Toyota", "Corolla")        # Create an object of Car, passing "Toyota" and "Corolla"
print(car1.var_1)                      # Access the 'var_1' attribute of car1, which is "Toyota"

# 7. Class Variables

    # Definition: These are variables that are shared among all instances of a class. 
    # They are defined at the class level and are not specific to any one object.
    # Context: Class variables are typically used for values that should be common to all instances of the class.

class Car:
    wheels = 4          # 'wheels' is a class variable (shared by all instances)

car1 = Car()
car2 = Car()
print(car1.wheels)      # Accessing class variable

