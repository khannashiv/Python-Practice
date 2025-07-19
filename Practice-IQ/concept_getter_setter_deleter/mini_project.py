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

    # Displaying the details of employee.
    def display(self):
        print(f"Employee name is: {self._name}, Employee age is: {self._age}, Employee monthly salary is: {self._salary}")
    

if __name__ == "__main__":

    # Creating objects for a class.
    emp_1 = employee("Shiv", 30, 1000)
    emp_2 = employee("Divi", 1, 11000)

    # Accessing the properties via getters
    emp_1.display()
    emp_2.display()

    # Modifying the properties of object-1 i.e.emp_1 via setters
    emp_1.name = "John"
    emp_1.display()

    # Modifying the properties of object-2 i.e. emp_2 via setters
    emp_2.salary = 2000
    emp_2.display()

    # Doing exception handling for modified peropertied of an object.
    try:
        emp_1.name="A"
    except ValueError as v:
        print(f"We need minimum 2 characters for employee name: {v}")

    try:
        emp_2.salary <= 0
    except ValueError as v1:
        print(f"Salary of an employee must be +ve: {v1}")
        
    finally:
        print("This block will execute for sure.")

    # Deleting the properties of both objects via deleters.
    del emp_1.name
    del emp_1.age
    del emp_1.salary

    del emp_2.name
    del emp_2.age
    del emp_2.salary

    # Checking the object after deletion
    print(emp_1.__dict__) 
    print(emp_2.__dict__) 
