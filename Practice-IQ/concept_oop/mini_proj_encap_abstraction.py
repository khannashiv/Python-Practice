# Mini Project: Employee Management System

# Project Description:

    # This system will manage employee information and their tasks. We'll implement:
    # Encapsulation: Using private attributes and providing getters/setters for controlled access.
    # Polymorphism: Using method overriding to implement different behaviors based on the type of employee.
    # Abstraction: Using an abstract class to define a common interface for different employee types.

# Abstract class for Employee (Abstraction)

from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, employee_id, salary):
        self._name         = name    # Encapsulated (private) attribute
        self._employee_id  = employee_id
        self._salary       = salary  # Encapsulated (private) attribute

    @abstractmethod
    def calculate_salary(self):
        pass

    # Getter for name (Encapsulation)
    def get_name(self):
        return self._name
    
    # Setter for name (Encapsulation)
    def set_name(self, name):
         self._name = name
    
    # Getter for employee_id (Encapsulation)
    def get_employee_id(self):
        return self._employee_id
    
    # Setter for employee_id (Encapsulation)
    def set_employee_id(self, employee_id):
        self._employee_id = employee_id
    
    # Getter for salary (Encapsulation)
    def get_salary(self):
        return self._salary
    
    # Setter for salary (Encapsulation)
    def set_salary(self, salary):
        self._salary = salary
    
    # Common method to display employee info.
    def display_info(self):
        print(f"Employee_Name: {self.get_name()}, Employee_ID: {self.get_employee_id()}, Employee_Salary: {self.get_salary()}")

# Derived class - FullTimeEmployee

class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id, salary, bonus):
        super().__init__(name, employee_id, salary)
        self._bonus = bonus

    def calculate_salary(self):
        # return self.get_salary() + self._bonus            # Wokring .
        return self._bonus + self._salary                   # Working.
    
    def display_info(self):
        super().display_info()
        print(f"Employee's bonus: {self._bonus}")
        print(f"Employee's total salary: {self.calculate_salary()}")

# Derived class - PartTimeEmployee

class PartTimeEmployee(Employee):
    def __init__(self, name, employee_id, hours_worked, hourly_wage):
        super().__init__(name, employee_id, 0)
        self._hours_worked = hours_worked
        self._hourly_wage  = hourly_wage

    def calculate_salary(self):
        return self._hours_worked * self._hourly_wage
    
    def display_info(self):
        super().display_info()
        print(f"Employee hourly wage: {self._hourly_wage}")
        print(f"Number of hours employee worked: {self._hours_worked}")
        print(f"Employee total salary: {self.calculate_salary()}")

print("\nFull-Time Employee Info:")
FTE_1 = FullTimeEmployee("Shiv", "123", 1000, 100)
FTE_1.display_info()

print(f"\nPrinting the wages for part-time employee: ")
PTE_1 = PartTimeEmployee("Divi", "456", 200, 20)
PTE_1.display_info()

# Explanation of Concepts:

    # 1. Encapsulation:

        # Encapsulation refers to the practice of restricting direct access to some of an object's attributes and methods.
        # In the Employee class, we’ve made the attributes (_name, _employee_id, _salary) private by prefixing them with an underscore (_), which is a convention indicating they should not be accessed directly from outside the class.
        # Instead, we provide getter and setter methods to get and modify the private attributes. This allows us to control the access and modification of the attributes.

            # Example:
                #  Getter and Setter methods:
                    # def get_name(self):
                    #     return self._name

                    # def set_name(self, name):
                    #     self._name = name

    # 2. Polymorphism:

            # Polymorphism allows methods to do different things based on the object it is operating on.
            # In this project, we have two types of employees: FullTimeEmployee and PartTimeEmployee. Both classes inherit from Employee, and both implement their own version of the method calculate_salary().
            # The method calculate_salary() is overridden in each derived class, and when called, it behaves differently depending on whether the employee is full-time or part-time.
            # This is an example of polymorphic behavior: calling the same method (calculate_salary()) but with different implementations depending on the object type.

            # Example:
                # def calculate_salary(self):
                #     return self.get_salary() + self._bonus  # Full-time salary

                # def calculate_salary(self):
                #     return self._hourly_rate * self._hours_worked  # Part-time salary

    # 3. Abstraction:

                # Abstraction is the concept of hiding the complex implementation details and exposing only the essential features of an object.
                # We use the abstract base class (Employee) to define a common interface (abstract methods like calculate_salary()) that all employee types must implement. This ensures that every employee type has a calculate_salary() method, but the implementation details of the method are hidden in the derived classes (FullTimeEmployee and PartTimeEmployee).
                # The Employee class defines the structure (abstraction) for all employees but leaves the specific implementation of certain behaviors (like calculating salary) to the derived classes.

                # Example:
                    # from abc import ABC, abstractmethod

                    # class Employee(ABC):
                    #     @abstractmethod
                    #     def calculate_salary(self):
                    #         pass

# More Points to note.

    # ABC: This stands for Abstract Base Class. It’s a module that helps in creating abstract classes in Python.
    # abstractmethod: This is a decorator used to define a method that must be implemented by any subclass.
    # Employee class is abstract, which means it cannot be instantiated directly. 
        # This means you cannot create an object of that class on its own.
        # It's a blueprint for other employee classes (like FullTimeEmployee and PartTimeEmployee).
        # It inherits from ABC to become an abstract class.
        # An abstract class is a class that contains one or more abstract methods.
        # An abstract method is a method that does not have an implementation in the abstract class itself, but it must be implemented by any non-abstract class that inherits from it.
        # Abstract classes are used to define common interfaces or behavior, but they are not intended to be instantiated directly.


    # Constructor (__init__):
        # Attributes (_name, _employee_id, _salary): These are encapsulated or private attributes.
        # The underscore (_) is just a convention to indicate they are "private" and should not be accessed directly.
        # The __init__ method is the constructor, which initializes these attributes when an object is created.

    # Abstract Method calculate_salary():
        # The @abstractmethod decorator marks this method as abstract, meaning any class that inherits from Employee must implement this method.
        # pass means that the method doesn't have any implementation in the Employee class; it must be defined in the derived classes (FullTimeEmployee, PartTimeEmployee).

    #  Encapsulation: Getter and Setter Methods:
        # For each attribute (name, employee ID, salary), there are getter and setter methods that allow access and modification of these attributes while keeping them "private".
        # These getter and setter methods allow:
            # Getters: To retrieve the value of the attribute.
            # Setters: To set or modify the value of the attribute.

    # FullTimeEmployee Class (Derived Class): This class inherits from Employee, making it a subclass. It is a concrete class that implements the abstract method calculate_salary().
        # Constructor (__init__):
            # super().__init__(name, employee_id, salary): This line calls the parent class's constructor to initialize the common attributes (name, employee ID, salary).
            # self._bonus = bonus: This initializes the bonus attribute for full-time employees.
            # Overriding calculate_salary():
                # This method is overridden from the abstract calculate_salary() method in the base class Employee.
                # It calculates the total salary for full-time employees by adding the bonus to the base salary.

    # Inherited Methods:
            # If a method is defined in the base class, the derived class automatically inherits it.
            # You can call that inherited method using self.method_name() in the derived class.

    # Inherited Attributes:
        # Similarly, any data member (attribute) defined in the base class can be accessed by the derived class using self.attribute_name.
                        

