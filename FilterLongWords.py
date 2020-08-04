"""
1.2 Write a function filter_long_words() that takes a list of words and an integer n and returns
the list of words that are longer than n.
"""


def filter_long_words(str, n) :
    word_list = []
    word = str.split(" ")
    for x in word :
        if len(x) > n :
            word_list.append(x)
    return word_list
    
sentence = "My dream is to become a data scientist"
print(sentence)
print(filter_long_words(sentence, 4))
