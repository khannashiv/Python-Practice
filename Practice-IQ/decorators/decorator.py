## Simple example of decorator function.

def my_dec(func):
    def wrapper():
        print("Something to perform before actual function.")
        func()
        print("Something to perform after actual function.")
    return wrapper


@my_dec                    
def say_hello():
    print ("This is the function that we want to decorate.")

say_hello()

# Expaination of above code .

# Step-by-Step Explanation:

    # Step 1: Defining the Decorator Function

        # def my_decorator(func):
        # def wrapper():
        #     print("Before the function is called.")
        #     func()  # Call the original function
        #     print("After the function is called.")
        # return wrapper

    # What's happening here?

        # The first function my_decorator(func) is the decorator.
        # The decorator function takes one argument, which is a function (func).

        # What is the decorator?

            # A decorator is a function that takes another function as an argument and returns a new function 
            # that usually adds some extra functionality to the original function.

            # In this case, my_decorator receives a function func as input and returns a new function wrapper that contains some extra logic.
            # Inside my_decorator, we define the wrapper() function. 
            # This function:

                # Prints "Before the function is called."
                # Calls the original function (func()).
                # Prints "After the function is called."

                # In essence:my_decorator wraps the original function with new behavior 
                # (print statements before and after the function call).
    
    # Step 2: Defining a Simple Function

        # def say_hello():
        #     print("Hello!")

        # Here, we define a simple function called say_hello, which just prints "Hello!" when called.

        # What does this mean?
            # say_hello() is the original function that we want to "decorate" or modify using the decorator.

    # Step 3: Applying the Decorator

        # say_hello = my_decorator(say_hello) --- > Code block 1

        # @my_dec                    --- > Code block 2
        # def say_hello():
        #     print ("This is the function that we want to decorate.")

        #  Here code block 1 is equal to code block 2.

    #   What is happening here?

    # This is where the decorator is applied to the function say_hello.

        # my_decorator(say_hello) takes the original say_hello function and wraps it inside the wrapper function defined in my_decorator.
        # The my_decorator function returns the wrapper function, which is then assigned to the say_hello variable.

    # Key Concept:

        # When you apply a decorator to a function, you are essentially replacing the original function 
        # with the new function (the wrapper function in this case), which has additional behavior.
        # So after this line, calling say_hello() will actually call the wrapper() function, not the original say_hello function.

    # Step 4: Calling the Decorated Function

        # say_hello()

            #   What's happening here?

            # Now when you call say_hello(), you are calling the wrapper function that was returned by my_decorator.
            # The wrapper function adds the extra print statements before and after 
            # calling the original say_hello() function.

            # Let's break down the order of events:

                #     The wrapper function starts executing.
                #     It first prints "Before the function is called.".
                #     Then, it calls the original say_hello() function (which prints "Hello!").
                #     Finally, the wrapper function prints "After the function is called.".

#         Summary of What Happened:

            # The decorator (my_decorator) was defined to add extra behavior before and after the function call.
            # say_hello() was wrapped by my_decorator, which returned the wrapper function containing the additional behavior.
            # When say_hello() was called, it actually invoked the wrapper function,
            #  which called the original say_hello() and added extra print statements before and after.