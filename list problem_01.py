def numbers(list):

    positive_numbers_list = []
    negative_numbers_list = []

    for num in list:

        if num >0:
            positive_numbers_list.append(num)
        elif num <0:
            negative_numbers_list.append(num)   
        else:
            pass
    return positive_numbers_list , negative_numbers_list

list1 = [2,-3,-10,4,7,0,10,-11,12]

positive_numbers_list, negative_numbers_list = numbers(list1)

print(f"{positive_numbers_list}\n{negative_numbers_list}")
 

 









