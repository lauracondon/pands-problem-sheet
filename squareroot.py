# squareroot.py
# this program asks the user to input a positive number
# and finds the square root of it, using the Newton Method
# Author: Laura Condon

#creates a function called sqrt 
def sqrt(x):
        # finds the approximate square root of the input
        approx = 0.5 * x
        # uses Newton's Method to find a better approximation of the square root
        better = 0.5 * (approx + x/approx)
        # repeats Newton's Method until the approx. square root no longer changes
        while better != approx:
            approx = better
            better = 0.5 * (approx + x/approx)
        return approx


# requests input from the user
num =  float(input("Please enter a positve number: "))
# throws an error message if they enter a negative number
if num < 0:
    print("That was a negative number! Please try again")
else:
    # calls the function sqrt
    sqrtNum = (sqrt(num))
    # prints the output rounded to one decimal place
    print("The square root of " + str(num) + " is approx. " + str(round(sqrtNum,1)))

