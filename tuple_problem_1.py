def max_min_number(number):

    max_number = max(number)
    min = number[0]

    for num in number:
        if num < min and num < max_number:
            min = num
    return max_number , min

numbers = (23,56,12,45,6,67,45,90,4,45)

max_number, min = max_min_number(numbers)

print(f"{max_number}\n{min}")
         
         
         

                 





 