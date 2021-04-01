# es.py
# This program reads in a text file and outputs the number of times the letter 'e' appears
# The program takes filename from an argument on the command line.
# Author: Laura Condon

# takes the filename from an argument on the command line
text_file = input("Please enter the name of your file: ")
# the file is opened as openFile in read mode, encoding is specified to ensure no errors when reading the file
with open(text_file, "r", encoding="utf8") as open_file:
    text_string = open_file.read()
    # checks for lowercase e
    num_of_e = text_string.count("e")
    # checks for uppercase e
    num_of_cap_e = text_string.count("E")
    # adds the two resulting integers together
    total_e = num_of_e + num_of_cap_e
    # prints the result
    print("The letter e appears in this document " + str(total_e) + " times")

