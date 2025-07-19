## Mini-Project: Function Call Logger and Performance Tracker ##

# This mini-project demonstrates how decorators can be applied to real-world use cases like logging, performance monitoring, and debugging. 
# In this example, we created a logging decorator that can be used on any function to log its inputs, outputs, and execution time. 
# This approach is highly flexible, reusable, and can easily be extended for other purposes like caching, access control, etc.

import time

def log_func_call(func):

    def wrapper(*args, **kwargs):

        print(f"Function name is: {func.__name__}")
        print(f"Arguments: {args}")
        print(f"Keyword arguments: {kwargs}")
        
        start_time = time.time()
        result     = func(*args, **kwargs)
        end_time   = time.time()

        print(f"Execution time is: {end_time - start_time : .4f} seconds")
        return result

    return wrapper

@log_func_call
def add(a, b):
    return a + b

# print(add(1, 2)) 

@log_func_call
def concat_str(str_1, str_2):
    return str_1 + " " + str_2

# print(concat_str("Hello", "Shiv...!!!"))

@log_func_call
def server_delay():
    time.sleep(2)
    return "Data Fetched..!!"

# print(server_delay())

# Method 1 : Test function calls

# print(server_delay())
# print(add(1, 2))
# print(concat_str("Hello", "Shiv...!!!"))

# Method 2 : Wrapping function calls inside a main() function.

def main():
    print(server_delay())                      # Test server_delay with sleep
    print(add(1, 2))                           # Test add function
    print(concat_str("Hello", "Shiv...!!!"))   # Test concat_str function

if __name__ == "__main__":
    main()                                     # Call the main function



#### ***Points to Note*** ####

        # In Python, every function is an object, and like any other object, it has several attributes.
        # One of the important attributes for a function object is __name__, which contains the name of the function as a string.
        # In the context of decorators, func.__name__ is typically used to get the name of the function that is being wrapped or modified by the decorator.
        # func.__name__ helps you log or track the name of the function being executed without hardcoding it. 
        # This is especially useful in decorators where the function name may vary.
        # Use return() when:
            # You need to pass a result back to the calling code, so it can be used later in your program
            # The result of the function needs to be stored or manipulated later in the program.
            # You want to return a value to be used by other functions or logic in the program.
        # Use print() when:
            # You want to display information directly to the user, such as debugging messages or logging output.
        # Summary of print & return.
            # print() will display intermediate information or results.
            # return() will provide the final result back to the caller.
        #  The .4f is a format specifier used in Python to control how numbers are displayed when printed, especially floating-point numbers.
            # Here's what .4f means:
                # .4: This specifies the precision of the number, i.e., the number of digits after the decimal point.
                # f:  This stands for floating-point numbers (used for numbers with a decimal point).
        #  The if __name__ == "__main__": statement is a Python convention used to control when certain code gets executed in a script.

            # To put it simply:
                # When a Python file is run directly, the __name__ variable is set to "__main__".
                # When a Python file is imported as a module into another script, the __name__ variable is set to the name of the file (without the .py extension).
                # if __name__ == "__main__": ensures that certain code in a script only runs when the script is executed directly, and not when it's imported into another script

# Possible Real-World Use Cases.

    #     API Request Logging : You can use decorators to log every API request and response along with the time taken. 
    #                            This is useful for debugging or performance monitoring in web applications.

    #     Database Query Logging : In a web application, you might want to log the execution time and results of every database query. 
    #                           A decorator could be used to wrap your database query functions to provide this functionality.

    #     Performance Monitoring : In long-running or computationally expensive processes, decorators can help you monitor 
    #                           how long certain functions or code blocks take to execute, helping with optimization.
