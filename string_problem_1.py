def palindrome_checker(names):
    name = names.lower()
    reversed_name = name[::-1]

    for ch in names:
        if name == reversed_name:
            return "Palinedrome"
        else:
            return "Not Palindrome"
     
name1 = "Mom"
name2 = "shuvo"
print(palindrome_checker(name1))
print(palindrome_checker(name2))
