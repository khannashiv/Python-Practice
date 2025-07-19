# my_dec    -->  Decorator which takes function as argument.
# say_hello -->  Original function or actual function whose functionality we want to change.

# Define a decorator function that takes another function 'func' as input

def my_dec(func):
    # This is the wrapper function that adds behavior before and after 'func' runs
    def wrapper():
        print("Print something before the actual function.")    # Pre-function behavior
        func()                                                  # Call the original function
        print("Print something after the actual function. ")    # Post-function behavior
    return wrapper                                              # Return the modified function with added behavior

# Define a simple function to be decorated
def say_hello():
    print("Hello ..&.. Hi !!")                                   # Original function behavior

# Method 1 : Where we are storing the outcomes to new variable i.e. decorated_func

# decorated_func = my_dec(say_hello)
# decorated_func()

# Method 2 : Where we are storing the outcomes in variable holding same name as that of original function i.e. say_hello

# Apply the decorator manually by reassigning 'say_hello' to the decorated version.
# This is equivalent to using @my_dec above the function definition.

say_hello = my_dec(say_hello)

# Now calling 'say_hello()' runs the wrapper, adding messages before and after the original content
say_hello()
