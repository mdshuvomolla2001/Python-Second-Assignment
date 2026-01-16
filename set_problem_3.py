def union_set(number1,number2):
    union_result = []

    for num in list1+list2:
        union_result.append(num)
    return set(union_result)
    
list1 = [1,3,4,6,7,8,10]
list2 = [2,3,7,9,10,11,12,14]

print(union_set(number1=list1,number2=list2))