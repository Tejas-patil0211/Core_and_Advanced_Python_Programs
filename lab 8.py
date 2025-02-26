Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Program to handle ZeroDivisionError exception
... 
... try:
...     # Taking user input
...     num = int(input("Enter a number: "))
... 
...     # Attempting division by zero (which raises an error)
...     result = num / 0  
... 
... # Handling the ZeroDivisionError
... except ZeroDivisionError:
...     print("Error: Division by zero is not allowed.")
... 
... # Else block executes only if no exception occurs
... else:
...     print("Result:", result)
... 
... # Finally block executes no matter what (useful for cleanup tasks)
... finally:
...     print("Execution completed.")
