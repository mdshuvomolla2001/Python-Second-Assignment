list1 = [1,3,4,5,6,7,8]
list2 = [2,4,5,7,10]
result = []
for num in list1:
    if num not in list2:
        result.append(num)
print(set(result))
        

