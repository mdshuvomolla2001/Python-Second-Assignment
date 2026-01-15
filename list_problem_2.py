
def numbers(list):

    first_max = None
    second_max = None

    for num in list:
        if first_max is None or first_max < num:
         
            second_max = first_max
            first_max = num
    
        elif (second_max is None or num > second_max) and num < first_max:
            second_max = num

    return second_max

list1 = [2,4,1,10,2,130,17]

first_max = numbers(list1)
print(first_max)

 


 


 
    