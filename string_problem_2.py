def word_reversal(sentence):
    splited_sentence =sentence.split()
    sentence_list = []
    for word in splited_sentence:
         reverse_word = word[::-1]
         sentence_list.append(reverse_word)
         sentence= ' '.join(sentence_list)
    return sentence

 
sentence1 = "the quick brown fox jumps over a lazy dog"

print(word_reversal(sentence1))




 