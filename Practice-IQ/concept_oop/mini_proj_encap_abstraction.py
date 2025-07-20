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
        # return self.get_salary() + self._bonus
        return self._bonus + self._salary
    
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
