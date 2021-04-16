# secondstring.py
# This programs asks a user to input a string 
# and then returns every second letter of it in reverse order
# Author: Laura Condon

# requests input from user 
# and stores it as a variable
sentence = input("Please enter a sentence: ")
# slice the string, with a step value of -1 to reverse it [1]
backwardsSentence = (sentence[::-1])
# slice it again with a step value of 2 
# to output every 2nd letter in the string [2]
print(backwardsSentence [::2])

# References
# [1] https://www.w3schools.com/python/python_howto_reverse_string.asp (accessed 03/02/2021) 
# [2] https://stackoverflow.com/questions/20847205/program-to-extract-every-alternate-letters-from-a-string-in-python (accessed 03/02/2021)
