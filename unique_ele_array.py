#  find the only element in an array that only occurs once.
def find_unique_element(array):
    unique_dict = {}
    for i in array:
        if i in unique_dict:
            del unique_dict[i]
        else:
            unique_dict[i] = 1
    if (len(unique_dict) == 1):
        return unique_dict.keys()
    elif (len(unique_dict) == 0):
        return "No unique element."
    else:
        return unique_dict.keys()


print(find_unique_element([2, 1, 5, 3, 6, 7, 2, 6, 8, 3]))
