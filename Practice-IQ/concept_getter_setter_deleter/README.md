<!-- 

 In Python, getter, setter, and deleter are methods that allow you to manage access to an object's attributes (also known as properties) in a controlled way. 
 
 They are commonly used to provide more control over how attributes are accessed or modified, often with the help of Python's built-in property() function or the @property decorator.

 These concepts help in:

    -- Encapsulation (hiding internal details).
    -- Customizing how data is retrieved (using getters).
    -- Validating data before it gets assigned to an attribute (using setters).
    -- Cleaning up resources when an attribute is deleted (using deleters).

    1. Getter:

        A getter is a method that is used to access the value of an attribute. It allows you to retrieve the value of a private attribute in a controlled manner or while keeping the data hidden.

        The @property decorator makes the method act like an attribute, allowing you to access it with the same syntax as a regular attribute (person.name and person.age).


    2. Setter:

        A setter is a method that is used to set or modify the value of an attribute. It provides a way to change the value of a private attribute while adding some validation or restrictions.

    3. Deleter:

        A deleter is a method that is used to delete an attribute. This gives you control over what happens when an attribute is deleted, such as releasing resources or logging the deletion.
 -->

<!-- 

In this Hands-On : Where we have code related to app.py

@property:

    This decorator turns the method into a getter. When you access person.name, Python automatically calls the name() method and returns the value of self._name.

@name.setter:

    This decorator turns the method into a setter. When you assign person.name = "Bob", Python automatically calls the name() setter method and assigns the value to self._name. We also validate that the name is at least 2 characters long.

@name.deleter:

    This decorator turns the method into a deleter. When you call del person.name, the name() deleter method is called. You can include any cleanup code in the deleter, like logging the deletion or releasing resources.

 -->

 <!-- 
 
 Ques : Why do we need to define del self._name and del self._age in the Deleter?

 Sol : 

    - In Python, when you use @property and its associated deleter, the del statement is used to actually remove the underlying attribute (like _name and _age) from the object.

    -  The deleter method doesn't automatically delete the attribute unless you explicitly tell it to do so.

    - So, the del self._name and del self._age lines inside the deleter methods are required because:

        - Deleting the property itself (like del person.name) doesn't automatically delete the underlying attribute (_name or _age).

        - The deleter method only triggers when you call del person.name or del person.age, but it needs explicit instructions inside the method to delete the actual object data that the property is managing.
    
  -->

  <!-- 
    Methods by which we can define getter & setter .

    Method-1 

        Explicit Getter and Setter Methods (the "manual" way):

            - This is the traditional approach where you define separate methods for getting and setting the values of attributes.

            - It’s simple, clear, and effective, especially when you don't need additional logic like validation, calculation, or dynamic behavior.
  
            class Employee:
                def __init__(self, name, employee_id, salary):
                    self._name = name
                    self._employee_id = employee_id
                    self._salary = salary

                def get_name(self):
                    return self._name

                def set_name(self, name):
                    self._name = name

                def get_employee_id(self):
                    return self._employee_id

                def set_employee_id(self, employee_id):
                    self._employee_id = employee_id

                def get_salary(self):
                    return self._salary

                def set_salary(self, salary):
                    self._salary = salary


            emp = Employee("Divi", "123", 50000)
            print(emp.get_name())  # Access via getter
            emp.set_name("Shiv")    # Modify via setter

    Method-2 

        Using @property Decorator (the "Pythonic" way):

            - The @property decorator allows you to access methods like attributes while still having the flexibility of a method behind the scenes.

            - This is often seen as the more Pythonic way to define getters and setters because it keeps the code concise and clean while still allowing for additional logic or validation if needed.

                class Employee:
                    def __init__(self, name, employee_id, salary):
                        self._name = name
                        self._employee_id = employee_id
                        self._salary = salary

                    @property
                    def name(self):
                        return self._name

                    @name.setter
                    def name(self, value):
                        self._name = value

                    @property
                    def employee_id(self):
                        return self._employee_id

                    @employee_id.setter
                    def employee_id(self, value):
                        self._employee_id = value

                    @property
                    def salary(self):
                        return self._salary

                    @salary.setter
                    def salary(self, value):
                        self._salary = value

                emp = Employee("Divi", "123", 50000)
                print(emp.name)     # Access via property (getter)
                emp.name = "Shiv"  # Modify via setter

   -->