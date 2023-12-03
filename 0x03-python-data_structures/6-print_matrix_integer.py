#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for num in range(len(matrix)):
        for element in range(len(matrix[num])):
            print("{:d}".format(matrix[num][element]), end="")
            if element != (len(matrix[num]) - 1):
                print(" ", end="")
        print()
