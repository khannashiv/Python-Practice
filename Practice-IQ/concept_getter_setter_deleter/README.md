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
 
 Ques : Why Do We Need to Define del self._name and del self._age in the Deleter?

 Sol : 

    - In Python, when you use @property and its associated deleter, the del statement is used to actually remove the underlying attribute (like _name and _age) from the object.

    -  The deleter method doesn't automatically delete the attribute unless you explicitly tell it to do so.

    - So, the del self._name and del self._age lines inside the deleter methods are required because:

        - Deleting the property itself (like del person.name) doesn't automatically delete the underlying attribute (_name or _age).

        - The deleter method only triggers when you call del person.name or del person.age, but it needs explicit instructions inside the method to delete the actual object data that the property is managing.
 
  -->