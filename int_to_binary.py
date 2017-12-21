#  Write a function that prints out the binary form of an int.
import pdb


def decimal_to_binary(decimal_int):
    binary_rep = ""
    pdb.set_trace()
    while decimal_int > 0:
        remainder = decimal_int % 2
        #  binary_rep = (binary_rep * 10) + remainder
        binary_rep += str(remainder)
        decimal_int = decimal_int // 2

    return binary_rep


print(decimal_to_binary(10))
