students_score = {
    "shuvo": 81,
    "asif": 75,
    "sajid": 78,
    "rafsan": 90,
    "atik": 85,
    "shakib": 85,
    "tushin": 69,
    "asik": 92,
    "sadim": 88,
    "samim": 60
}
dic = {}
for name, mark in students_score.items():
    if mark in dic:
        dic[mark] += [name]
    else:
        dic[mark] = [name]
print(dic)
    

 

