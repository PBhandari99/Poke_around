def most_frequent_integer(in_array):
    frequency_dict = {}
    most_frequent_pair = [0,0]
    for i in in_array:
        if i in frequency_dict:
            frequency_dict[i] += 1
        else:
            frequency_dict[i] = 1
            
        if frequency_dict[i] > most_frequent_pair[1]:
            most_frequent_pair[0] = i
            most_frequent_pair[1] = frequency_dict[i]

    return most_frequent_pair[0] 

