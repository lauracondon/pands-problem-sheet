## Weekly Problem Sheets for Programming & Scripting

### Table of Contents

1. [Introduction](https://github.com/lauracondon/pands-problem-sheet/blob/main/README.md#introduction)
2. [Week 2 - bmi.py](https://github.com/lauracondon/pands-problem-sheet/blob/main/README.md#week-2---bmipy)
3. [Week 3 - secondstring.py](https://github.com/lauracondon/pands-problem-sheet/blob/main/README.md#week-3---secondstringpy)
4. [Week 4 - collatz.py](https://github.com/lauracondon/pands-problem-sheet/blob/main/README.md#week-4---collatzpy)
5. [Week 5 - weekday.py](https://github.com/lauracondon/pands-problem-sheet/blob/main/README.md#week-5---weekdaypy)
6. [Week 6 - squareroot.py](https://github.com/lauracondon/pands-problem-sheet/blob/main/README.md#week-6---squarerootpy)
7. [Week 7 - es.py](https://github.com/lauracondon/pands-problem-sheet/blob/main/README.md#week-7---espy)
8. [Week 8 - plottask.py](https://github.com/lauracondon/pands-problem-sheet/blob/main/README.md#week-8---plottaskpy)

____________________________________________________________________________________________________________________

### Introduction

This github repository contains the weekly tasks completed for the 2021 Programming and Scripting module for GMIT's HDip in Science in Computing (Data Analytics).

This README contains a description of each task, followed by an explanation of its code and then a list of references consulted. 

____________________________________________________________________________________________________________________

### Week 2 - bmi.py

#### Task: 

1. Write a program that calculates somebody's Body Mass Index (BMI). Call the file bmi.py.
2. The inputs are the person's height in centimetres and weight in kilograms.
3. The output is their weight divided by their height in metres squared.

Test Input: 

$ python bmi.py

Please enter your weight in kilograms: 65

Please enter your height in centimetres: 180

Your BMI is 20.06

#### Code Explanation: 

I enclosed my BMI program within a try/except statement so that if the user mistakenly enters a string it will show them a relevant error message. 

The user is prompted to input their height and weight. This input is converted from a string to a float, so that mathematical operations can be performed on it. 

To find their BMI, the user's weight is divided by their height and then squared. As height was entered in centimetres, it is first divided by 100 to convert it into metres. The answer is stored in the variable 'bmi'.

Finally, the variable 'bmi' is rounded to two decimal places and converted to a string, so that it can be concatenated with another string and then displayed to the user.

#### References:
- Stack Overflow. *How to round to 2 decimals with Python?* https://stackoverflow.com/questions/20457038/how-to-round-to-2-decimals-with-python (accessed 30/01/2021)
- Python.org. *Errors and Exceptions - Invalid Input Error using Try/Except.*  https://docs.python.org/3/tutorial/errors.html (accessed 30/01/2021)

____________________________________________________________________________________________________________________

### Week 3 - secondstring.py

#### Task: 

1. Write a program that asks a user to input a string and outputs every second letter in reverse order.

Test Input: 

$ python secondstring.py

Please enter a sentence: The quick brown fox jumps over the lazy dog.

.o zletrv pu o wr cu h

#### Code Explanation:

This program uses string slicing in order to output the reverse of every second letter in the inputted sentence. 

First, the user is prompted to enter a sentence. This input is stored as a string in the variable 'sentence'.

A new variable called 'backwardsSentence' is created to store the reverse of the string. The inputted string is sliced with a step value of -1 in order to reverse it. Essentially this code is saying start at the last character in the string and 'step' backwards one character at a time. 

The same technique as above is used to return every second letter. This time the step value is set to 2, meaning that every second letter in the now reversed string is 'jumped' over. The result is outputted to the user. 

#### References:
- w3schools. *Python - Slicing Strings* https://www.w3schools.com/python/python_strings_slicing.asp (accessed 03/02/2021)
- w3schools. *How to Reverse a String in Python.* https://www.w3schools.com/python/python_howto_reverse_string.asp (accessed 03/02/2021) 
- Stack Overflow. *program to extract every alternate letters from a string in python?* https://stackoverflow.com/questions/20847205/program-to-extract-every-alternate-letters-from-a-string-in-python (accessed 03/02/2021)

____________________________________________________________________________________________________________________

### Week 4 - collatz.py

#### Task: 

1. Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation:
   - At each step calculate the next value by taking the current value and:
      - if it is even, divide it by two. 
      - if it is odd, multiply it by three and add one.
      - Have the program end if the current value is one.

Test Input: 

$ python collatz.py

Please enter a positive integer: 10

10 5 16 8 4 2 1

#### Code Explanation:

The user is prompted to enter a positive integer. Their input is converted from a string to an integer and stored in the variable 'value'.

A simple if statement is used to display an error message if they enter a negative integer by mistake. 

The rest of the program is enclosed in a while loop. First it checks again that the user has entered a positive integer (greater than zero).

Next it determines if the user has entered an even value by using the modulo operator to check if the remainder of division by two is equal to zero. If it is, it divides the value by two (using // so that a whole number is returned) and the while loop returns to the start.  

If the value is odd (the remainder of division does not equal zero) and it is not equal to one, it it multiplied by three and then one is added to it. The while loop returns to the start.

If the value is equal to one, in order to end the while loop (and hence the program) one is minused from it. As the value is now zero, the while loop ends and the successive values of the calculation on the inputted value are outputted to the user. Break could have been used here instead to end the loop. In either case, it is important to include a stop clause otherwise the loop would just continue indefinitely until it causes a stack overflow error.

### References: 
 - w3schools. *Basics of While Loops.* https://www.w3schools.com/python/python_while_loops.asp (accessed 10/02/2021)
 - Real Python. *Python "while" Loops (Indefinite Iteration).* https://realpython.com/python-while-loop/ (accessed 26/03/2021)

____________________________________________________________________________________________________________________

### Week 5 - weekday.py

#### Task: 

1. Write a program that outputs whether or not today is a weekday.

Test Input: 

An example of running this program on a Thursday:

$ python weekday.py

Yes, unfortunately today is a weekday.

An example of running it on a Saturday:

$ python weekday.py

It is the weekend, yay!

#### Code Explanation:

To start with, the datetime module is imported - this is a built-in module in Python that allows you to work with dates and times in your program. As the program only needs to determine what day of the week it is, only the date class from datetime is imported. 

Next 'date.today()' is used to determine what the current date is. The answer is stored in the variable 'today' and expressed in the format 'year, month, day'.

To determine what day of the week it is, '.weekday()' is used on the variable 'today' and the output is stored as the variable 'what_day'. 

When using '.weekday()' the days of the week are expressed not as strings but as integers (with Monday == 0 and Sunday == 6). The program uses a simple if statement to determine what today is. If today is less than 5 it is a weekday and if it is anything else it is the weekend. The program outputs a different specified message to the user depending on the answer to above. 

#### References:
 - Programiz. *Python datetime.* https://www.programiz.com/python-programming/datetime (accessed 19/02/2021) 
 - Pythonic. *Weekday Function In Python.* https://pythontic.com/datetime/date/weekday (accessed 19/02/2021) 

____________________________________________________________________________________________________________________

 ### Week 6 - squareroot.py

 #### Task: 
1. Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.
2. Create your own sqrt function, called sqrt, that does this and do not use the built in functions x ** .5 or math.sqrt(x).

Test Input: 

$ python squareroot.py

Please enter a positive number: 14.5

The square root of 14.5 is approx. 3.8

#### Code Explanation:

The function 'sqrt' is defined. The function first finds the approximate square root of the input 'x' by multiplying it by 0.5 and stores it in the variable 'approx'. 

Next it finds a more exact approximation of the square root by using Newton's Method. It does this by taking the approximate square root and adding the input 'x' divided by the approximate square root to it. This is then multiplied by 0.5 and stored in the variable 'better'. 

With Newton's Method, the more times you run it the more exact the approximation gets. You could use iteration to apply it over and over, however, you'd have to guess at the number of times to apply it. Eventually, with Newton's Method, it will reach a point where the current approximation is the same as the previous one - at which point you can stop applying it. 

This program uses a while loop to do this. While the 'better' variable does not equal the 'approx' variable, it will continue to apply Newton's Method. Once they do equal each other, the loop ends. 

Now that the function has been defined, it can be applied to the user's input and the output can then be displayed. Here a combination of a while loop with a try-except statement is used to catch input errors. If a user mistakenly enters a string or enters a negative number, it will display a relevant error message and prompt them until they enter a positive number. 

### References: 

 - Runestone Academy - How to Think Like a Computer Scientist. *Newton's Method.* https://runestone.academy/runestone/books/published/thinkcspy/MoreAboutIteration/NewtonsMethod.html (accessed 28/02/2021)
 - techbeamers. *How to Best Use Try Except in Python* https://www.techbeamers.com/use-try-except-python/ (accessed 01/04/2021)
 - GeeksforGeeks. *Python | Assertion Error* https://www.geeksforgeeks.org/python-assertion-error/ (accessed 01/04/2021)

____________________________________________________________________________________________________________________

 ### Week 7 - es.py 

#### Task: 
1. Write a program that reads in a text file and outputs the number of e's it contains.
2. The program should take the filename from an argument on the command line.

Test Input: 

$ python es.py 

Please enter the name of your file: moby-dick.txt

The letter e appears in this document 1211 times

#### Code Explanation:

The user is asked to input the name of the file they wish to check. The file is opened in read mode - as this is the default open mode it doesn't need to be specified in the code. 

A for loop is used to check the text in the file one line at a time - rather than read the whole file into memory at once. 

The program uses 'text_string.count' to check for the specified character in the file - in this case it checks for lowercase and uppercase 'e' separately and then adds the two figures together. The total is then outputted to the user. 

### References: 

 - Real Python. *Reading and Writing Files in Python* https://realpython.com/read-write-files-python/ (accessed 04/03/2021)
 - Real Python. *Working With Files in Python* https://realpython.com/working-with-files-in-python/ (accessed 04/03/2021)
 - w3schools. *Python File Open* https://www.w3schools.com/python/python_file_handling.asp (accessed 04/03/2021)
 - GeeksforGeeks. *Count the number of times a letter appears in a text file in Python* https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/ (accessed 04/03/2021)
 - codegrepper. *how to count the occurrence of a word in string python* https://www.codegrepper.com/code-examples/python/how+to+count+the+occurrence+of+a+word+in+string+python (accessed 04/03/2021)
 - Stack Overflow. *UnicodeDecodeError: 'charmap' codec can't decode byte X in position Y: character maps to <undefined>* https://stackoverflow.com/questions/9233027/2021unicodedecodeerror-charmap-codec-cant-decode-byte-x-in-position-y-character (accessed 04/03/2021)
 - Standford University. *Python File Reading* https://web.stanford.edu/class/archive/cs/cs106a/cs106a.1204/handouts/py-file.html (accessed 02/04/2021)

  ### Week 7 - moby-dick.txt
  
  The text in this document was sourced from Project Gutenburg for use in testing the es.py program. 

 - Project Gutenburg. *Moby Dick - Chapter 1* https://www.gutenberg.org/files/2701/2701-h/2701-h.htm (accessed 04/03/2021)

____________________________________________________________________________________________________________________

 ### Week 8 - plottask.py
1. Write a program called plottask.py that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.
2. Some marks will be given for making the plot look nice.

#### Code Explanation:

The first step is to import the modules required for this program - numpy and matplotlib. 'As' is used here to specify how to call the modules for use throughout the program. 

The range of values for 'x', in this case 0-4, and the values of the functions (f,g,h) we want to plot are specified. 

Each function is plotted on the graph using the plot command. The resulting graph is saved to a file named 'plottask.png' and also displayed to the user in a pop up window. 

The above commands are enough to create and display a graph but there are a lot of additional things you can add to your code to improve readability and to make it more aesthetically pleasing. For my graph, I specified what font I wanted using font-family. I added a grid behind the graph and specified how I wanted it to look. I added labels for each axes and a title, as well as a legend to clearly inform the viewer which line is which function. 

When choosing the colour of my lines, I choose a colour palette geared towards colour blind users (tableau color blind 10). I converted the colour codes from rgb to hex for easier entry in Python. Then, in order to try make it more obvious that the lines were overlapping I set two of them to be dashed in style, with different widths and distance between each dash. 

### References: 

- Real Python. *What Is NumPy?* https://realpython.com/tutorials/numpy/ (accessed 10/03/2021)
- Real Python. *NumPy arange(): How to Use np.arange()* https://realpython.com/how-to-use-numpy-arange/ (accessed 10/03/2021)
- Tutorial's Point. *MATLAB - Plotting* https://www.tutorialspoint.com/matlab/matlab_plotting.htm (accessed 10/03/2021)
- Kite. *How to plot multiple lines on the same graph in Matplotlib in Python* https://www.kite.com/python/answers/how-to-plot-multiple-lines-on-the-same-graph-in-matplotlib-in-python (accessed 10/03/2021)
- Tableau Public. *Color Palettes with RGB Values* https://public.tableau.com/profile/chris.gerrard#!/vizhome/TableauColors/ColorPaletteswithRGBValues (accessed 20/03/2021)
- Matplotlib. *Gallery* https://matplotlib.org/stable/gallery/index.html (accessed 20/03/2021)
- rgbtohex. https://www.rgbtohex.net/rgb/ (accessed 20/03/2021)
- Matplotlib. *Customizing dashed line styles* https://matplotlib.org/stable/gallery/lines_bars_and_markers/line_demo_dash_control.html (accessed 22/03/2021)
- Stack Overflow. *How to change the font of the legend?* https://stackoverflow.com/questions/43814540/how-to-change-the-font-of-the-legend (accessed 22/03/2021)
- Python Basics. *Matplotlib Line Chart* https://pythonbasics.org/matplotlib-line-chart/ (accessed 22/03/2021)
- Github - Jake VanderPlas.*Python Data Science Handbook - Simple Line Plots* https://jakevdp.github.io/PythonDataScienceHandbook/04.01-simple-line-plots.html (accessed 22/03/2021)
- Stack Overflow. *How do I draw a grid onto a plot in Python?* https://stackoverflow.com/questions/8209568/how-do-i-draw-a-grid-onto-a-plot-in-python (acessed 22/03/2011)