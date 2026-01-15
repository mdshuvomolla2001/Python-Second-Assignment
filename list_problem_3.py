def rotated_list(list,k):
    list_length = len(list)
    k = k % (list_length)
    rotated = list[-k:] + list[:-k]
    return rotated

list1 = [1,2,3,4,5]
print(rotated_list(list1,2))






 

    
