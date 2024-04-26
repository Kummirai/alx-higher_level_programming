<<<<<<< HEAD
# 0x11. Python - Network #1

The purpose of this project is to master the following concepts:
- How to fetch internet resources with the Python package urllib
- How to decode urllib body response
- How to use the Python package requests #requestsiswaysimplerthanurllib
- How to make HTTP GET request
- How to make HTTP POST/PUT/etc. request
- How to fetch JSON resources
- How to manipulate data from an external service

## Task Requirements
- All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
- Your code should use the PEP 8 style (version 1.7.*)
- All your modules should have a documentation (```python3 -c 'print(__import__("my_module").__doc__)'```)
- You must use ```get``` to access to dictionary value by key (it won’t throw an exception if the key doesn’t exist in the dictionary)
- Your code should not be executed when imported (by using ```if __name__ == "__main__":```)

---
File | Task
---|---
0-hbtn_status.py | Script that fetches ```https://intranet.hbtn.io/status```
1-hbtn_header.py | Script that sends a request to the URL passed in and displays the value of the ```X-Request-Id``` variable
2-post_email.py | Script that sends a ```POST``` request to the URL passed in with the email as a parameter and displays the body of the response
3-error_code.py | Script that sends a request to the URL passed in and displays the body of the response
4-hbtn_status.py | Script that fetches ```https://intranet.hbtn.io/status``` using the package ```requests```
5-hbtn_header.py | Script that sends a request to the URL passed in and displays the ```X-Request-Id``` variable, using the packages ```requests``` and ```sys```
6-post_email.py | Script that takes in a URl and email address, sends a ```POST``` request to the passed in URL with the email as parameter, and displays the body of the response -- using the packages ```requests``` and ```sys```
7-error_code.py | Script that sends a request to the URL passed in and displays the body of the response -- using the packages ```requests``` and ```sys```
8-json_api.py | Script that takes in a letter and sends a ```POST``` request to ```http://0.0.0.0:5000/search_user``` witht he letter as a parameter
9-starwars.py | Script that takes in a string and sends a search request to the Star Wars API
10-my_github.py | Script that takes your Github credentials and uses the Github API to display your ```id```
=======
