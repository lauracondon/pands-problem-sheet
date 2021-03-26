## Weekly Problem Sheets for Programming & Scripting

### Week 2 - bmi.py

#### Task: 

1. Write a program that calculates somebody's Body Mass Index (BMI). Call the file bmi.py
2. The inputs are the person's height in centimetres and weight in kilograms.
3. The output is their weight divided by their height in metres squared.

Test Input: 

$ python bmi.py
Enter weight: 65
Enter height: 180
BMI is 20.06.

#### Code Explanation: 

I enclosed my BMI program within a try/except statment so that if the user mistakenly entered a string it would show them a relevant error message. 

The user is prompted to input their height and weight. This input is converted from a string to a float, so that we can perform mathematical operations on it. 

To find the BMI, the user's weight is divided by their height and then squared. As height was entered in centimetres, it is first divided by 100 to convert it into metres. The answer is stored in the variable 'bmi'.

Finally, The variable 'bmi' is rounded to two decimal places and converted to a string, so that it can be concatenated with another string, then displayed to the user.

#### References:
- Stack Overflow. *How to round to 2 decimals with Python?* https://stackoverflow.com/questions/20457038/how-to-round-to-2-decimals-with-python (accessed 30/01/2021)
- Python.org. *Errors and Exceptions - Invalid Input Error using Try/Except.*  https://docs.python.org/3/tutorial/errors.html (accessed 30/01/2021)

____________________________________________________________________________________________________________________

### Week 3 - secondstring.py

#### Task: 

1. Write a program that takes asks a user to input a string and outputs every second letter in reverse order.

Test Input: 

$ python secondstring.py
Please enter a sentence: The quick brown fox jumps over the lazy dog.
.o zletrv pu o wr cu h

#### Code Explanation:

#### References:
w3schools. *Python - Slicing Strings* https://www.w3schools.com/python/python_strings_slicing.asp (accessed 03/02/2021)
w3schools. *How to Reverse a String in Python.* https://www.w3schools.com/python/python_howto_reverse_string.asp (accessed 03/02/2021) 
Stack Overflow. *program to extract every alternate letters from a string in python?* https://stackoverflow.com/questions/20847205/program-to-extract-every-alternate-letters-from-a-string-in-python (accessed 03/02/2021)

### Week 4 - collatz.py
10/02/2021 - Note: I'm not entirely happy with my solution, although it does work. I feel like there's probably an easier way to achieve the same outcome. In particular I'd like to go back and redo the way the program ends when the value becomes one as I feel I'm missing something obvious there!

Sources used: 
 - [Basics of While Loops](https://www.w3schools.com/python/python_while_loops.asp) accessed on Wednesday February 10th 2021

 ### Week 5 - weekday.py

 Sources used: 
 - [Datetime Module](https://www.programiz.com/python-programming/datetime) accessed on Friday February 19th 2021
 - [The Weekday Function](https://pythontic.com/datetime/date/weekday) accessed on Friday February 19th 2021

 ### Week 6 - squareroot.py
 28/02/2021 - Note: I would like to go back and add some code that will restart the program if the user enters a negative number, rather than just throw an error message and end it

 Sources used: 
 - [Newton Method](https://runestone.academy/runestone/books/published/thinkcspy/MoreAboutIteration/NewtonsMethod.html) accessed on Sunday February 28th 2021
 - [Limiting to one decimal place](https://stackoverflow.com/questions/20457038/how-to-round-to-2-decimals-with-python) accessed on Sunday February 28th 2021

 ### Week 7 - es.py 

 Sources used: 
 - [Real Python - Reading and Writing Files](https://realpython.com/read-write-files-python/ ) accessed on Thursday March 4th 2021
 - [Real Python - Working with Files in Python](https://realpython.com/working-with-files-in-python/) accessed on Thursday March 4th 2021
 - [w3schools - Handling Files in Python](https://www.w3schools.com/python/python_file_handling.asp) accessed on Thursday March 4th 2021
 - [geeksforgeeks - Counting the No. of Times a Letter Appears in a Text File](https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/) accessed on Thursday March 4th 2021
 - [codegrepper - Counting the Occurence of a Word in a String](https://www.codegrepper.com/code-examples/python/how+to+count+the+occurrence+of+a+word+in+string+python) accessed on Thursday March 4th 2021
 - [Stack Overflow - Handling a Decode Error](https://stackoverflow.com/questions/9233027/2021unicodedecodeerror-charmap-codec-cant-decode-byte-x-in-position-y-character) accessed on Thursday March 4th 2021

  ### Week 7 - moby-dick.txt
 - [Moby Dick - Chapter One. Sourced from Project Gutenberg](https://www.gutenberg.org/files/2701/2701-h/2701-h.htm) accessed on Thursday March 4th 2021

 ### Week 8 - plottask.py
10/03/2021 - Note: I need to comment my code and also add some extra formatting to it to make it look nicer

I used the tableau color blind 10 palette to choose colours for my lines. I converted them from rgb to hex for easier entry. In order to make it more obvious that the lines were overlapping I set two of them to be dashed in style, with different widths and distance between each dash. 

References: 

https://realpython.com/tutorials/numpy/ (accessed 10/03/2021)
https://realpython.com/how-to-use-numpy-arange/ (accessed 10/03/2021)
https://www.tutorialspoint.com/matlab/matlab_plotting.htm (accessed 10/03/2021)
https://www.kite.com/python/answers/how-to-plot-multiple-lines-on-the-same-graph-in-matplotlib-in-python(accessed 10/03/2021)

https://www.rgbtohex.net/rgb/ (accessed 20/03/2021)
https://public.tableau.com/profile/chris.gerrard#!/vizhome/TableauColors/ColorPaletteswithRGBValues (accessed 20/03/2021)
https://matplotlib.org/stable/gallery/index.html (accessed 20/03/2021)

https://matplotlib.org/stable/gallery/lines_bars_and_markers/line_demo_dash_control.html (accessed 22/03/2021)
https://stackoverflow.com/questions/43814540/how-to-change-the-font-of-the-legend (accessed 22/03/2021)
https://pythonbasics.org/matplotlib-line-chart/ (accessed 22/03/2021)
https://jakevdp.github.io/PythonDataScienceHandbook/04.01-simple-line-plots.html (accessed 22/03/2021)
https://stackoverflow.com/questions/8209568/how-do-i-draw-a-grid-onto-a-plot-in-python (acessed 22/03/2011)