#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for element in range(0, x):
        try:
            if isinstance(my_list[element], int):
                print("{:d}".format(my_list[element]), end="")
                count = count + 1
        except (ValueError, TypeError):
            continue
    print()
    return (count)
