# module_example.py

def greet(name):
    print(f"Hello, {name}!")

def add(a, b):
    return a + b

# This code will run only if the script is executed directly
if __name__ == "__main__":
    print("This code is running from the main script!")
    greet("Alice")
    print(f"Sum of 5 and 3 is: {add(5, 3)}")
