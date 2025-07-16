################## Exception handling in python ############

# Example 1. FileNotFound

# Problem : Sample Code which will throw an exception / error i.e. FileNotFoundError

# file =open("a.txt", "r")       # Non working scenario, file does not exist and  will throw an error.
# content = file.read()
# print(content)

# Solution : 

# Method 1.

# try:
#     # file = open("./iq.py", "r")  # Working scenario where file exist
#     file =open("a.txt", "r")       # Non working scenario, file does not exist and  will throw an error.
#     content = file.read()
#     print(content)
# # except :                         # Working .
# except FileNotFoundError:          # Also working .
#     # This block runs if an error occurs in the try block
#     print("Check if the given file exists or not.")
# else:
#     # This block runs if no exception was raised in the try block
#     print(" File found !!")
#     file.close()                               # Closing the file after reading it.
#     print("closing the file now.") 
# finally:
#      # This block runs always, whether an exception was raised or not.
#     print("Finally will get executed always.")

# Method 2.

# try:
#     with open ("a.txt", "r") as file:
#         content=file.read()
#         print(content)
# except:
#     print("File not found on the path defined above.")
# else:
#     print("file found successfully.")
# finally:
#     print("This block will execute always.")

####################################################################################

# Example 2. 

# Problem : Sample Code which will throw an exception / error i.e. NameError

# if num%2 == 0:
#     print("Given number is even number.")
# else:
#     print("Given number is odd in nature.")

# Solution : 

# try:
#     if num%2 == 0:
#         print("Given number is even number.")
#     else:
#         print("Given number is odd in nature.")
# # except:                                               # working.
# except NameError:                                       # working.
#     print("If 'num' not defined in that case exception is raised ")
# else:
#     print("Logic to check odd / even is succesful.")
# finally:
#     print("This block will execute always.")

################################################################################# 

# Example 3.

# Problem: Sample Code which will throw an exception / error i.e. ZeroDivisionError

# a = 10
# b = 0
# c = a/b
# print(c)

# Solution : 

# try:
#     a=10
#     b=0
#     c=a/b
#     print(c)
# except ZeroDivisionError:
#     print("Division by zero is not possible.")
# else:
#     print("Division is Successful.")
# finally:
#     print("This block will execute always.")

##########################################################################################################

# Example 4:

# Problem : Raise custom exception if input is lesser than certain value.

# Solution : 

# my_input = int(input("Please enter numeric value of your choice: "))

# try:
#     if my_input < 5000:
#         print("You don't have sufficient balance.")
#         raise Exception (" first custom exception.")
# # except:
# #     print("Custom exception has raised.")
# except Exception as e:
#     print(f"Custom exception has raised,{e}")
# else:
#     print("Sufficient balance")
# finally:
#     print("This block will execute always.")

#####################################################################

# NOTE : Custom exceptions in Python are not restricted to using the Exception class. 
# While Exception is the base class for all built-in exceptions, you can define and raise your own 
# custom exception by creating a class that inherits from Exception (or any other built-in exception class).

###################################################################### 
# Example 5: Basic Custom Exception

# class InsufficientBalanceError(Exception):
#     def __init__(self, message="Balance is insufficient"):
#         self.message=message
#         super().__init__(self.message)

# # Raising the custom exception.
# try:
#     raise InsufficientBalanceError("You don't have enough funds.")
# except InsufficientBalanceError as e:
#      print(f"Custom Exception Raised: {e}")

# Step-by-step Explanation:

    # Defining the Custom Exception:

        #  The class InsufficientBalanceError is defined as a subclass of the built-in Exception class.
        #  The __init__ method is overridden to customize the exception. 
        #  The default message is "Balance is insufficient", but we can provide a custom message when raising the exception.

    # Raising the Exception:

        # Inside the try block, we raise the custom exception InsufficientBalanceError by using raise InsufficientBalanceError("You don't have enough funds").
        # This statement causes the program to exit the try block and jump to the except block because the exception was raised.

    # Catching the Custom Exception:

        # In the except block, we catch the raised exception using the class name InsufficientBalanceError.
        # The exception object is stored in the variable e, which holds the message ("You don't have enough funds").
        # The message is printed as "Custom Exception Raised: You don't have enough funds".

########################################################### 

# Example 6: Custom Exception with a Custom Error Code

# class InvalidTransactionError(Exception):
#     def __init__(self, message="Invalid Transaction", error_code=1001):
#         self.message = message
#         self.error_code = error_code
#         super().__init__(self.message)

#     def __str__(self):
#         # return f"{self.message} (Error Code: {self.error_code})" # Original
#         return f"{self.message} {self.error_code}" # Modified.

# # Raising the custom exception with an error code
# try:
#     raise InvalidTransactionError("Transaction not allowed", 2001)
# except InvalidTransactionError as e:
#     print(f"Custom Exception: {e}")

# Step-by-step Explanation:
    # Defining the Custom Exception:

        # InvalidTransactionError is a subclass of Exception.
        # The __init__ method is customized to accept a message (default: "Invalid Transaction") and an error_code (default: 1001).
        # In the __str__ method, we define how the exception will be printed when it is caught. 
        # This method returns a string that includes both the message and the error code.

    # Raising the Custom Exception:

        #  Inside the try block, we raise the exception with a custom message "Transaction not allowed" and an error code 2001.
        #  This is done using: raise InvalidTransactionError("Transaction not allowed", 2001)
        #  This statement raises the exception, which is caught by the except block.

# Catching the Custom Exception:

        # The exception is caught by the except block where we print the exception object (e).
        # The __str__ method is automatically called, which returns the formatted string "Transaction not allowed (Error Code: 2001)".


########################################################### 

# Example 7: Multiple Custom Exceptions.

class LowBalanceError(Exception):
    pass

class UnauthorizedAccessError(Exception):
    pass

balance = 201

try:
    if balance == 100:
        raise UnauthorizedAccessError("Access denied.")
     
    if balance < 200:
        raise LowBalanceError("Not enough balance.")

except LowBalanceError as e:
    print(f"Low Balance Error: {e}")

except UnauthorizedAccessError as e:
    print(f"Unauthorized Access Error: {e}")

############################################333 

# Step-by-step Explanation:

    # Defining Multiple Custom Exceptions:

        # We define two custom exceptions:

            #     LowBalanceError: This will be raised if the balance is too low.
            #     UnauthorizedAccessError: This will be raised if access is denied due to specific conditions.

# Raising Exceptions Based on Conditions:

    # Inside the try block:

        # The program checks if the balance is less than 200. If it is, the LowBalanceError exception is raised.
        # If the balance is exactly 100, the UnauthorizedAccessError exception is raised.

    # In this case, since balance is 100, the UnauthorizedAccessError exception will be raised.

# Catching the Exceptions:

    # We have two except blocks:

        # If a LowBalanceError is raised, the first except block catches it and prints the error.
        # If an UnauthorizedAccessError is raised, the second except block catches it and prints the error.

    # In this case, the UnauthorizedAccessError will be caught and printed: "Unauthorized Access Error: Access denied."

################################################################## 

# Summary of Key Concepts:

# Custom Exception:

    # A custom exception is created by inheriting from the base Exception class (or any other built-in exception class).
    # You can override the __init__ method to add custom attributes (like message, error_code, etc.).
    # The __str__ method can be overridden to customize how the exception is printed.

# Raising a Custom Exception:

    # You can raise a custom exception using the raise keyword.
    # You pass the custom exception class and any parameters (like a message or error code) when raising the exception.

# Catching and Handling Custom Exceptions:

    # Custom exceptions can be caught using the except block, just like built-in exceptions.
    # You can have multiple except blocks to handle different types of custom exceptions.

############################## 
