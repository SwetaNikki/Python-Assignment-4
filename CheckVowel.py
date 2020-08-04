"""
2.2 Write a Python function which takes a character (i.e. a string of length 1) and returns True if
it is a vowel, False otherwise.

"""

#function to check if given character is vowel or not
def check_vowel(char) :
    if (char=='a' or char=='e' or char=='i' or char=='o' or char=='u'):
        return True
    else:
        return False
            
#Taking input character from user            
char = input("Enter a character(alphabet): ");

#print if return value if True
if (check_vowel(char)):
    print(char," is a vowel")
else:
    print(char," is not a vowel")
