# Mini Project: Vehicle Management System
# Project Description:
    # We will have a base class Vehicle that contains common attributes (like make, model, color, etc.) and methods (like display_info()).
    # We will then define two derived classes: Car and Bike. 
    # These will inherit from Vehicle and will have their own additional attributes and methods (like num_doors for Car and type_of_bike for Bike).
    # We'll demonstrate method overriding (where the derived class has its own version of a method) and method inheritance (using the base class methods).

class vehicle():
    def __init__(self, make, model, color):
        self.make  = make
        self.model = model
        self.color = color

    def display_info(self):
        print(f"Vehicle info is: {self.make} {self.model}, color: {self.color}")

# Derived class - Car
class car(vehicle):
    def __init__(self, make, model, color, num_doors):
        # Call the constructor of the base class (Vehicle)
        super().__init__(make, model, color)
        # Specific attribute for Car
        self.num_doors = num_doors

    def display_info(self):
        # Override display_info to include Car-specific details
        super().display_info()          # Call base class method
        print(f"Number of doors for this car is: {self.num_doors}")
    
    def honk(self):
        # A method specific to the Car class
        print("Car honking: Beep Beep !!")

# Derived class - Bike
class bike(vehicle):
    def __init__(self, make, model, color, type_of_bike):
        # Call the constructor of the base class (Vehicle)
        super().__init__(make, model, color)
        # Specific attribute for bike.
        self.type_of_bike = type_of_bike

    def display_info(self):
        # Override display_info to include Bike-specific details
        super().display_info()          # Call base class method
        print(f"Type of bike is: {self.type_of_bike}")

    def start_engine(self):
         # A method specific to the Bike class
         print("Bike engine starting... Vroom Vroom!")

print("\nDisplaying car information as follow..")
car_1 = car("Maruti", "Swift", "White", 4)
car_1.display_info()
car_1.honk()

print("\nDisplaying bike information as follow..")
bike_1 = bike("Harley", "Davidson", "Black", "Sports")
bike_1.display_info()
bike_1.start_engine()


# Key OOP Concepts Demonstrated:

    # Inheritance: Car and Bike inherit from the base class Vehicle.
    # Method Overriding: The display_info() method is overridden in both Car and Bike classes to add additional details specific to each class.
    # Method Calling (super): The super() function is used to call the method of the base class from the derived class, allowing for reuse of code while adding new functionality.
    # Polymorphism: Even though display_info() is used in both Car and Bike, it behaves differently based on the class type, demonstrating polymorphism.


# Explanation:

# 1. Base Class Vehicle:

    # The Vehicle class is the base class that contains common attributes like make, model, and color.
    # It also has a method display_info() which is used to display the basic information about the vehicle.

# 2. Derived Class Car:

    # The Car class inherits from the Vehicle class using class Car(Vehicle):.
    # It has a specific attribute num_doors, which is unique to cars.
    # The display_info() method is overridden to include the car-specific attribute num_doors, in addition to the common vehicle information (called using super()).
    # It also has a unique method honk(), which is specific to cars.

# 3. Derived Class Bike:

    # The Bike class also inherits from Vehicle.
    # It has a specific attribute type_of_bike, which can be "Sport", "Cruiser", etc.
    # The display_info() method is overridden to display the bike-specific attribute type_of_bike, in addition to the common vehicle details.
    # It has a unique method start_engine(), which is specific to bikes.