#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_new_list = []
    for elements in range(0, list_length):
        result = 0
        try:
            result = my_list_1[elements] / my_list_2[elements]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            my_new_list.append(result)
    return (my_new_list)
