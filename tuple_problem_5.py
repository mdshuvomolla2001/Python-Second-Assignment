
def concatenate_tuples(tuple1,tuple2):
    combine_result = []
    for num in tuple1,tuple2:
        combine_result.extend(num)
    return tuple(combine_result)

t1 = (1,2,3)
t2 = (4,5,6)
result = concatenate_tuples(t1,t2)
print(result)