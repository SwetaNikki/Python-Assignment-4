"""
2.1 Write a Python program using function concept that maps list of words into a list of integers
representing the lengths of the corresponding words.
Hint: If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4]
Here 2,3 and 4 are the lengths of the words in the list.

"""

word_list = ["I","want","to","be","a","Data","Scientist"]
def word_length_list(long_list):
    result = map(lambda word: len(word), long_list)
    return list(result)

print("Word List        =>  {}".format(word_list)) 
print("Word Length list =>  {}".format(word_length_list(word_list))) 


