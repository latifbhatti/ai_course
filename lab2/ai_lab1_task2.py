# Write a function named analyze_sentence that takes a sentence as input and returns a dictionary containing the following information:
# the total number of words, the total number of characters (excluding spaces), the average word length, and a list of unique words.

import string
def analayze_sentance(sentance):
    words=0
    charecter=0
    word = sentance.split()
    unique_words = list(set(word))
    alphabets = list(string.ascii_letters)  
    for i in sentance:
        if i==' ':
            words+=1
        elif (i in alphabets):
            charecter+=1
        else:
            pass
    dict = {"words":words,"charecter":charecter,"unique word list":unique_words,"average word":words/charecter}
    return dict

a=analayze_sentance('my roll number is 21b-029-se')
print(a)

        

