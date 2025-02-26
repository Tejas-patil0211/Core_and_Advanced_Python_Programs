Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Program to prompt user for an integer and handle invalid input
... 
... try:
...     # Prompting user for an integer
...     num = int(input("Enter an integer: "))  
...     print("You entered:", num)
... 
... # Handling invalid input (non-integer values)
... except ValueError:
...     print("Error: Invalid input. Please enter a valid integer.")
