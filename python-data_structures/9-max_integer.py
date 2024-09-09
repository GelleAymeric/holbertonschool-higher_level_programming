#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == "":
        return None
    else:
        
        max_integer = my_list[0]
        for i in my_list:
            if i > max_integer:
                max_integer = i
        return max_integer
