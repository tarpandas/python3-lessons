def max_num(custom_list):
    max = custom_list[0]
    for number in custom_list:
        if number > max:
            max = number
    
    return max