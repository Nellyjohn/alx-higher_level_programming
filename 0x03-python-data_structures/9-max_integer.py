#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        largest_int = my_list[0]
        for integer in my_list:
            if integer > largest_int:
                largest_int = integer
    return (largest_int)
