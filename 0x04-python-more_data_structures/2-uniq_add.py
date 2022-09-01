#!/usr/bin/python3
def uniq_add(my_list=[]):
    #insert list to a set
    unique_int = set(my_list)

    #Convert the set to a list
    unique_list = list(unique_int)
    total = 0
    #transverse through the list
    for i in range(0, len(my_list)):
        total = total + my_list[i]
        print(i)
        return(total)
