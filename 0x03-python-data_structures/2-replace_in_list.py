#!/user/bin/pyhton3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return(my_list)
    if len(my_list) - 1 < idx:
        return(my_list)
    del(my_list[idx])
    my_list.insert(idx, element)
    return(my_list)
