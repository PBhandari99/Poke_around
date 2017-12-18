#  Find the common elements of 2 int arrays.
def find_common(array1, array2):
    array1_dict = {}
    common_elem = []
    for i in array1:
        if i not in array1_dict:
            array1_dict[i] = 1
    for j in array2:
        if j in array1_dict:
            common_elem.append(j)
    return common_elem


print(find_common([1, 2, 5, 3, 7, 4, 3], [5, 3, 7, 2, 8, 6]))
