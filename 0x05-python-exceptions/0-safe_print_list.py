#!/usr/bin/python3

'''
Function that printa list
'''

def safe_print_list(my_list=[], x=0):
    try:
        for i in range(0, x):
            print("{}".format(my_list[i]), end="")
    except IndexError:
        print()
        return(i)
    print()
    return(x)
