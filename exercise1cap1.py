def equal_list(first_list, second_list):
    
    if len(first_list) != len(second_list):
        return 'Different lists.'
    
    for index, item in enumerate(first_list):
        if item != second_list[index]:
            return 'Different lists.'
    
    return 'The lists are equals!!!'


first_list = [1,2,3,4,5]
second_list = [1,2,3,4,5]

result = equal_list(first_list,second_list)
print(result)