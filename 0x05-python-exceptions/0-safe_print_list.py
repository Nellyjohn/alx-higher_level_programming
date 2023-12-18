#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for element in range(0, x):
        try:
            if count < x:
                print("{}".format(my_list[element]), end="")
                count = count + 1
        except IndexError:
            break
    print()
    return (count)
