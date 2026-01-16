def index_lookup(numbers,num):
    
    for i in range(len(numbers)):
        if numbers[i] == num:
            return i
    return "Not found"       

numbers1 = (1,5,8,45,34,20,3,8)

print(index_lookup(numbers1,20))





