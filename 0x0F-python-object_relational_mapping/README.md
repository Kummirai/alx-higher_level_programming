# 0x0F. Python - Object-relational mapping

The purpose of this project is to learn the following concepts:

- How to connect to a MySQL database from a Python script
- How to SELECT rows in a MySQL table from a Python script
- How to INSERT rows in a MySQL table from a Python script
- What ORM means
- How to map a Python Class to a MySQL table

## Requirements for Python scripts
- All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
- Your files will be executed with MySQLdb version 1.3.x
- Your files will be executed with SQLAlchemy version 1.2.x
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- Your code should use the PEP 8 style (version 1.7.*)
- The length of your files will be tested using wc
- All your modules should have a documentation ```(python3 -c 'print(__import__("my_module").__doc__)')```
- All your classes should have a documentation ```(python3 -c 'print(__import__("my_module").MyClass.__doc__)')```
- All your functions (inside and outside a class) should have a documentation ```(python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')```
- You are not allowed to use ```execute``` with sqlalchemy

---
File | Task
---|---
0-select_states.py | Script that lists all ```states``` from the database ```hbtn_0e_0_usa```
1-filter_states.py | Script that lists all ```states``` with a ```name``` starting with ```N``` from the database ```hbtn_0e_0_usa```
2-my_filter_states.py | Script that takes an argument and displays all values in the ```states``` table of ```hbtn_0e_0_usa``` where ```name``` matches the argument
3-my_safe_filter_states.py | Script safe from MySQL injections that takes in arguments and displays all values in the ```states``` table ```hbtn_0e_0_usa``` where ```name``` matches the argument
4-cities_by_state.py | Script that lists all ```cities``` from the database ```hbtn_0e_4_usa```
5-filter_cities.py | Script that takes in the name of a state as an argument and lists all ```cities``` of that state using the database ```hbtn_0e_4_usa```
model_state.py | Script that contains the class definition ```State``` and an instance ```Base = declarative_base()```
7-model_state_fetch_all.py | Script that lists all ```States``` objects from the database ```hbtn_0e_6_usa```
8-model_state_fetch_first.py | Script that prints the first ```State``` object from the database ```hbtn_0e_6_usa```
9-model_state_filter_a.py | Script that lists all ```State``` objects that contain the letter ```a``` from the database ```hbtn_0e_6_usa```
10-model_state_my_get.py | Script that prints the ```State``` object with the ```name``` passed as argument from the database ```hbtn_0e_6_usa```
11-model_state_insert.py | Script that adds the ```State``` object "Louisiana" to the database ```hbtn_0e_6_usa```
12-model_state_update_id_2.py | Script that changes the name of a ```State``` object from the database ```hbtn_0e_6_usa```
13-model_state_delete_a.py | Script that deletes all ```State``` objects with a name containing the letter ```a``` from the database ```hbtn_0e_6_usa```
model_city.py | Script that contains the class defintion of a ```City```
14-model_city_fetch_by_state.py | Script that prints all ```City``` objects from the database ```hbtn_0e_14_usa``
