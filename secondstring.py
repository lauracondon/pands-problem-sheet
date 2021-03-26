# secondstring.py
# This programs asks a user to input a string and then returns every second letter of it in reverse order
# Author: Laura Condon

# requests input from user and stores it as a variable
sentence = input("Please enter a sentence: ")
# slice the string, with a step value of -1 to reverse it 
backwardsSentence = (sentence[::-1])
# slice it again with a step value of 2 in order to 'jump' over every 2nd letter in the now reversed string
print(backwardsSentence [::2])

