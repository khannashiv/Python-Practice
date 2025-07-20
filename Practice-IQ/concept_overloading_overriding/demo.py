# 1. Method Overloading (Compile-time Polymorphism) || Static Polymorphism

# Example 1.

# Method-1 : Using only function.

def add(*args):
    counter = 0
    for i in args:
        counter += i
    return counter

print(add(1))
print(add(1, 2))
print(add(3, 4, 5))

# Method-2 : Using function, class & object.

class Calculator:
    def add(self, *args):
        counter = 0
        for i in args:
            counter += i
        return counter

calc = Calculator()
print(calc.add(5))      
print(calc.add(5, 3)) 

# 2. Method Overriding (Runtime Polymorphism). || Dynamic Polymorphism

# In Python, method overriding typically occurs in the context of inheritance and classes, but we can simulate 
# overriding by redefining a function in the same namespace or scope. In this case, we’ll override a function with a different implementation.

# Method-1 : Using only function.

# Base function
def greet():
    print("Hello from Base!")

# Override the base function in the same scope
def greet():
    print("Hello from Overridden Function!")

# Calling the function
greet()  # Output will be from the overridden function

# Method-2 :  Using function, class & object.

class animal():
    def speak(self):
        print("Sound of diffrent animals.")

class dog(animal):
    def speak(self):
        print("Dog barks..!!")

class cat(animal):
    def speak(self):
        print("Cat meaw..!!")

# One way of creating objects & calling respective member functions.
obj_dog = dog()
obj_dog.speak()

obj_cat = cat()
obj_cat.speak()

# Second way of creating objects & calling member function.
common_obj=[dog(), cat()]
for i in common_obj:
    i.speak()