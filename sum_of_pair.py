def sum_of_pair(input_array, req_sum):
    # key is the required interger for it to make the sum and value is the index that 
    # is to be added to make the sum. 
    pair_dict = {}
    for i in range(len(input_array)):
        pair_dict[req_sum - input_array[i]] = i 

    for i in range(len(input_array)):
        if input_array[i] in pair_dict and i != pair_dict[input_array[i]]:
            return [i, pair_dict[input_array[i]]]


