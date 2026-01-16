
def character_counter(sentence):
    sentence = sentence.lower()
    dic = {}
    for ch in sentence:
        if ch !=" ":

           if ch in dic:
                dic[ch] += 1
           else:
                dic[ch] = 1
    return dic
 
 
sentence1 = "the quick brown fox jumps over a lazy dog"
sentence2 =  "Iam shuvo"

print(character_counter(sentence1))
print(character_counter(sentence2))

