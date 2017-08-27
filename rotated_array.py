def check_rotated(first_array, second_array):
    if len(first_array) !=  len(second_array):
        return False
    start = first_array.index(second_array[0])
    for i in range(len(second_array)):
        if second_array[i] != first_array[start%len(first_array)]:
            return False
        else:
            start += 1
    return True

