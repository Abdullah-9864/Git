import pyjokes   
# pyjokes is a Python library for generating programming jokes. It provides a collection of jokes that can be used to lighten the mood while coding or to share with fellow programmers.
    
# the differece between modules and libraries in Python is that a module is a single file containing Python code, while a library is a collection of modules that provide specific functionality. A module can be imported and used in a Python program, while a library is typically installed and then imported as needed.
print("printing jokes...")
joke= pyjokes.get_joke()
print(joke)