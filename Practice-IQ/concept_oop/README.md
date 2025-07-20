#### Concepts of Object-Oriented Programming (OOP) ####

**Class:**  
A blueprint for creating objects. It defines attributes (data) and methods (functions) that describe the behavior and state of its objects.

**Object:**  
An instance of a class. Objects hold real data and can perform actions defined by their class.

**Methods:**  
Functions defined inside a class that operate on its data and define the behavior of objects.

**Inheritance:**  
A mechanism for creating new classes from existing ones. The new (derived) class inherits attributes and methods from the base class, enabling code reuse and extension.

**Encapsulation:**  
The practice of restricting direct access to some of an object's attributes and methods. This is achieved using access modifiers (public, protected, private) and getter/setter methods to control how data is accessed or modified.

**Abstraction:**  
Hiding complex implementation details and showing only the necessary features of an object. Abstract classes and methods define interfaces that must be implemented by derived classes.

**Polymorphism:**  
The ability to use a unified interface for different data types. Methods can be overridden or overloaded to provide specific behavior in derived classes.

---

**Variables:**  
Named references to data.

**Attributes / Data Members:**  
Variables associated with a class.  
- **Instance Variables:** Tied to a specific object (instance).  
- **Class Variables:** Shared across all instances of the class.

**Arguments:**  
Values passed to a function when it is called.

**Parameters:**  
Variables in the function definition that receive the argument values.

**Local Variables:**  
Variables defined inside a function, limited to that function’s scope.

---

<!-- 

My Questions & Doubts from mini_proj_encap_abstraction.py

**Q1:** Why are getter & setter methods sometimes defined without using `@property` or `@name.setter`?  
**A:** There are multiple ways to implement getters and setters in Python. Using explicit methods is one approach; decorators like `@property` provide a more Pythonic way but are not mandatory.

**Q2:** What does `super().__init__(name, employee_id, salary)` do in a derived class?  
**A:** It calls the base class constructor, passing the parameters so the derived class can use and initialize them.

**Q3:** Why can derived classes access `calculate_salary()`?  
**A:** If `calculate_salary()` is an abstract method in the base class, derived classes must implement it, enforcing a contract for behavior.

**Q4:** Can I use `return self._bonus + self._salary` instead of `return self.get_salary() + self._bonus`?  
**A:** Yes, if you have direct access to the attributes. Using getter methods is preferred for encapsulation.

**Q5:** Can I use private data members & member functions within a class?  
**A:** Yes, private members (prefixed with `_` or `__`) are accessible within the class.

-->
