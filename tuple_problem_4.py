def tuple_pair_sum(numbers):
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            if((numbers[i] + numbers[j])%2 == 0):
                    return ((numbers[i],numbers[j]))

numbers_1 = (1,2,3,4)
print(tuple_pair_sum(numbers_1))
    

    
     