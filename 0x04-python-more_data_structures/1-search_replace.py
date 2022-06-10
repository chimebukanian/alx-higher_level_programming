#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list_copy = []
    for i in range(len(my_list)):
        if my_list[i] == search:
            list_copy.append(replace)
        else:
            list_copy.append(my_list[i])
    return list_copy
