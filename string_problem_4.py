string = "banana apple strawberries mango"
result = ""
for ch in string:
    if ch ==" ":
        result += " " 
    elif ch in result:
        pass
    else:
        result += ch
       
print(result)

       