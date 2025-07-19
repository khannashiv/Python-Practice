# Project Overview:

    # In this project, we'll simulate a small Employee Management System where we have:

        # Employee Class: A class that stores details about employees.
        # Getters and Setters: For accessing and updating the employee's name, age, and salary.
        # Deleters: To manage cleaning up the employee records when they're deleted.

class employee():
    def __init__(self, name, age, salary):
        self._name   = name
        self._age    = age
        self._salary = salary

    # Getter for name attribute.
    @property
    def name(self):
        return self._name
    
    # Setter for name attribute.
    @name.setter
    def name(self, value):
        if len(value) >= 2:
            self._name = value
        else:
            raise ValueError ("Name of the employee must has atleast 2 characters.")

    @name.deleter
    def name(self):
        print ("Deleting name...")
        del self._name
    
    # Getter for age attribute.
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value > 0:
            self._age = value
        else:
            raise ValueError ("Age should be a positive number.")
        
    @age.deleter
    def age(self):
        print("Deleting age...")
        del self._age
    
    # Getter for salary attribute.
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, value):
        if value > 0:
            self._salary = value
        else:
            raise ValueError ("Salary received by an employee must be +ve")

    @salary.deleter
    def salary(self):
        print("Deleting salary...")
        del self._salary
    
employee_1 = employee("Shiv", 30, 5000)
employee_2 = employee("Divi", 3, 1000)

# Accessing the properties via getters
print(employee_1.name)
print(employee_1.age)
print(employee_1.salary)

# Modifying the properties via setters
employee_1.name = "Nick"
print(employee_1.name)

employee_1.age = 22
print(employee_1.age)

employee_1.salary = 1100
print(employee_1.salary)

# Deleting the properties via deleters.
del employee_1.name
del employee_1.age
del employee_1.salary

# Checking the object after deletion
print(employee_1.__dict__) 

# print(employee_2.name)
# print(employee_2.age)
# print(employee_2.salary)


    