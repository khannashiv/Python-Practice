<!-- 

In this handson we have 2 python files i.e. main_example.py as well as module_example.py

Case 1 : 

1. Run module_example.py directly:

    Open your terminal or command line, navigate to the folder location & run module_example.py i.e. python module_example.py

    Output shows :

        This code is running from the main script!
        Hello, Alice!
        Sum of 5 and 3 is: 8

    Here’s what happens:

         -- When module_example.py is run directly, __name__ is set to "__main__", so the block of code inside if __name__ == "__main__": is executed.

        -- It prints "This code is running from the main script!", calls the greet("Alice") function, and prints the result of add(5, 3).

Case 2 : 

2.  Run main_example.py (which imports module_example.py):

        Now, run the main_example.py script: python main_example.py

    Output will be : Direct function call result: 5

    Here’s what happens:

        -- When main_example.py is executed, it imports module_example.py.

        -- However, because the script module_example.py is imported and not run directly, the code inside the if __name__ == "__main__": block is skipped. Therefore, it does not print "This code is running from the main script!", "Hello, Alice!", or the sum.

        -- It only runs the function add(2, 3) that was called directly from main_example.py.

 ** Key Takeaways ** :

    When you run module_example.py directly:

        The __name__ variable is set to "__main__", so the code inside the if __name__ == "__main__": block executes.

    When you run main_example.py and import module_example.py:

        The __name__ variable in module_example.py is set to "module_example", so the code inside the if __name__ == "__main__": block does not execute. Instead, only the functions and variables that are explicitly imported and called (like add(2, 3)) are executed.

 -->