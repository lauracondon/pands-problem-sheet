# squareroot.py
# this program asks the user to input a positive number
# and finds the square root of it, using the Newton Method
# Author: Laura Condon

#creates a function called sqrt 
def sqrt(x):
        # finds the approx. square root of the input
        approx = 0.5 * x
        # uses Newton's Method to find a better approx. of the square root [1]
        better = 0.5 * (approx + x/approx)
        # repeats it until the approx. square root no longer changes
        while better != approx:
            approx = better
            better = 0.5 * (approx + x/approx)
        return approx

# try/except with a while loop [2]
# if the user enters the wrong type of input 
# the prompt is repeated until they enter a positive integer 
while True:
    try:
        #requests input from the user
        num =  float(input("Please enter a positive number: "))
        # checks if number is positive using assertion
        assert num > 0 
    # if it's not a postive number, throws an assertion error [3]
    # and requests input again
    except AssertionError:
        print("That was a negative number. Please try again")
        continue
    # throws an error message if user enters a string 
    # and requests input again
    except ValueError:
        print("That was a string. Please try again")
        continue
    else:
        # calls the function sqrt
        sqrt_num = (sqrt(num))
        # prints the output rounded to one decimal place 
        print("The square root of " + str(num) + " is approx. " + str(round(sqrt_num,1)))
        # breaks out of the while loop
        break

# References 
# [1] https://runestone.academy/runestone/books/published/thinkcspy/MoreAboutIteration/NewtonsMethod.html (accessed 28/02/2021)
# [2] https://www.techbeamers.com/use-try-except-python/ (accessed 01/04/2021)
# [3] https://www.geeksforgeeks.org/python-assertion-error/ (accessed 01/04/2021)
