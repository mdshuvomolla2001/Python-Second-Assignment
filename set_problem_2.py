def common_elements(numbers_1,numbers_2):
    common_numbers = []
    for num in  numbers_1:
        if num in numbers_2:
            common_numbers.append(num)
    return set(common_numbers)

list1 = [1,3,4,6,7,8,10]
list2 = [2,3,7,9,10,11,12,14]

print(common_elements(numbers_1=list1,numbers_2=list2))
           
 

 