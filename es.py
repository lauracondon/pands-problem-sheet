# es.py
# This program reads in a text file 
# and outputs the number of times the letter 'e' appears
# The program takes filename from an argument on the command line.
# Author: Laura Condon

# takes the filename from an argument on the command line
text_file = input("Please enter the name of your file: ")
# the file is opened as open_file in read mode 
# encoding is specified to ensure no errors when reading the file [1]
with open(text_file, encoding="utf8") as open_file:
    # this checks the file one line at a time [2]
    for line in open_file:
        text_string = open_file.read()
            # checks for lowercase e [3]
        num_of_e = text_string.count("e") 
            # checks for uppercase e
        num_of_cap_e = text_string.count("E")
            # adds the two resulting integers together
        total_e = num_of_e + num_of_cap_e
            # prints the result
        print("The letter e appears in this document " + str(total_e) + " times")

# References 
# [1] https://stackoverflow.com/questions/9233027/2021unicodedecodeerror-charmap-codec-cant-decode-byte-x-in-position-y-character (accessed 04/03/2021)
# [2] https://web.stanford.edu/class/archive/cs/cs106a/cs106a.1204/handouts/py-file.html (accessed 02/04/2021)
# [3] https://www.codegrepper.com/code-examples/python/how+to+count+the+occurrence+of+a+word+in+string+python (accessed 04/03/2021)

