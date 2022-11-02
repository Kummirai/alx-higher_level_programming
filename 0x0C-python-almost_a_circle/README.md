# 0x0C. Python - Almost a circle

This project is a review of Python as well as a warm up to the upcoming AirBnB project. In this project, we review:

- Import
- Exceptions
- Class
- Private attribute
- Getter/Setter
- Class method
- Static method
- Inheritance
- Unittest
- Read/Write file

As well as learn:
- ```args``` and ```kwargs```
- Serialization/Deserialization
- JSON

## What should be learned from this project
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function

## Requirements for Python scripts
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the PEP 8 style (version 1.7.*)
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should be documented: ```python3 -c 'print(__import__("my_module").__doc__)'```
- All your classes should be documented: ```python3 -c 'print(__import__("my_module").MyClass.__doc__)'```
- All your functions (inside and outside a class) should be documented: python3 ```-c 'print(__import__("my_module").my_function.__doc__)'``` and ```python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'```

## Requirements for Python unit tests

For this project, unit tests will be created instead of doctest:

- All your test files should be inside a folder tests
- You have to use the unittest module
- All your test files should be python files (extension: .py)
- All your test files and folders should start with test_
- Your file organization in the tests folder should be the same as your project: ex: for models/base.py, unit tests must be in: tests/test_models/test_base.py
- All your tests should be executed by using this command: python3 -m unittest discover tests
- You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base.py
- We strongly encourage you to work together on test cases so that you don’t miss any edge case

---
File | Task
---|---
tests/ | All files in this folder have classes and methods that were unit tested and PEP 8 validated
models/base.py, models/__init__.py | This is the "base" of all other classes in this project
models/rectangle.py | A class ```Rectangle``` which inherits from the ```Base``` class
models/square.py | A class ```Square``` which inherits from the ```Rectangle``` class

## Author
Francesca Cantor