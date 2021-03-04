# es.py
# This program reads in a text file and outputs the number of times the letter 'e' appears
# The program takes filename from an argument on the command line.
# Author: Laura Condon

# takes the filename from an argument on the command line
textFile = input("Please enter the name of your file: ")
# the file is opened as openFile in read mode, encoding is specified to ensure no errors when reading the file
with open(textFile, "r", encoding="utf8") as openFile:
    textString = openFile.read()
    # checks for lowercase e
    numOfE = textString.count("e")
    # checks for uppercase e
    numOfCapE = textString.count("E")
    # adds the two resulting integers together
    totalE = numOfE + numOfCapE
    # prints the result
    print("The letter e appears in this document " + str(totalE) + " times")


    # https://realpython.com/read-write-files-python/ (accessed 4th March 2021)
    # https://realpython.com/working-with-files-in-python/ (accessed 4th March 2021)
    # https://www.w3schools.com/python/python_file_handling.asp (accessed 4th March 2021)
    # https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/
    # https://www.codegrepper.com/code-examples/python/how+to+count+the+occurrence+of+a+word+in+string+python (accessed 4th March 2021)
    # https://stackoverflow.com/questions/9233027/unicodedecodeerror-charmap-codec-cant-decode-byte-x-in-position-y-character (accessed 4th March 2021)
    # https://www.gutenberg.org/files/2701/2701-h/2701-h.htm (accessed 4th March 2021)
