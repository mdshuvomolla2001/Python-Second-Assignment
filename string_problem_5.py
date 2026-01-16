def anagram_checker(words_1,words_2):
    
    words_1 = sorted(words_1.lower())

    words_2 = sorted(words_2.lower())

    if words_1 == words_2:
        return "Anagram"
    else:
        return "Not anagram"

print(anagram_checker(words_1 = "Silent",words_2= "Listen"))
                     

 
