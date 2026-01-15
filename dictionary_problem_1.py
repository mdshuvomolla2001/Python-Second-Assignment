def numbers_list(numbers):
    dic = {}
    for num in numbers:
        if num in dic:
            dic[num] +=1
        else:
            dic[num] = 1
    return dic

number_list1 = [2,4,6,3,2,6,7,12,89,65,45,45,67,64,2,4,7,12,65,66,45,45,12]

dic = numbers_list(number_list1)

print(dic)