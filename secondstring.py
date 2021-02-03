# secondstring.py
# This programs asks a user to input a string and then returns every second letter of it in reverse order
# Author: Laura Condon

# requests input from user and stores it as a variable
sentence = input("Please enter a sentence: ")
# use a slice that steps backwards by -1 to reverse the string, and stores it as a new variable
backwardsSentence = (sentence[::-1])
# use a slice that 'steps' over every 2nd letter to return every second letter in the string
print(backwardsSentence [::2])
