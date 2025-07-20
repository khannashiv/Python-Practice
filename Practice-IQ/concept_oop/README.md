#### Concepts of OOP ####

    # Class: A blueprint that defines attributes (data) and methods (functions).
    # Object: An instance of a class that holds real data and can perform actions.
    # Methods: Functions inside a class that define the behavior of the objects.
    # Inheritance: Creating new classes that inherit from existing ones to reuse code.
    # Encapsulation: Controlling access to attributes using public, protected, and private attributes.

    # Variables: General term for any named reference to data.
    # Data Members / Attributes: Variables associated with a class (instance variables).
    # Arguments:  Values passed to a function when it is called.
    # Parameters: Variables in the function definition that receive the argument values.
    # Local Variables:    Variables defined inside a function, limited to that function’s scope.
    # Instance Variables: Data members tied to a specific object (instance).
    # Class Variables:    Variables that belong to the class itself, shared across all instances.

   <!-- 

My Questions & Doubts form mini_proj_encap_abstraction.py

    Ques 1: We generally define getter & setter using @property or @name.setter but here we are not using those things. Why so ? -- > Generally there are couple of ways to define getter & setter this is 1 of the way as we have learnt in the project.

    Ques 2 : When I write this i.e. super().__init__(name, employee_id, salary) under drived class this means it's importing all the parameters from base class to derive call right, so that we can use these parameters inside drive class? -- > Yes

    Ques 3: calculate_salary() we are able to access this function under drive classes because it's abstract method, which is a kind of compulsion to use under drive classes ? -- > Yes

    Ques 4 : Can I also use this statement i.e. return self._bonus + self._salary  instead of return self.get_salary() + self._bonus since we have already called salary parameter from above class ? -- > Yes

    Ques 5: Can I use private data members & member functions within a class ? -- > Yes.

    -->