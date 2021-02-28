# squareroot.py
# this program asks the user to input a positive number
# and finds the square root of it, using the Newton Method
# Author: Laura Condon

#creates a function called sqrt 
def sqrt(x):
        # finds the approximate square root of the input
        approx = 0.5 * x
        # uses the Newton Method to find a better approximation of the square root
        better = 0.5 * (approx + x/approx)
        # repeat the Newton Method until the approx. square root no longer changes
        while better != approx:
            approx = better
            better = 0.5 * (approx + x/approx)
        return approx

num =  float(input("Please enter a positve number: "))
if num < 0:
    print("That was a negative number! Please try again")
else:
    #call the function sqrt
    sqrtNum = (sqrt(num))
    print("The square root of " + str(num) + " is approx. " + str(round(sqrtNum,1)))

# References: 
# Newton Method - https://runestone.academy/runestone/books/published/thinkcspy/MoreAboutIteration/NewtonsMethod.html
# accessed 28/02/2021
# Limiting to one decimal place - https://stackoverflow.com/questions/20457038/how-to-round-to-2-decimals-with-python
# accessed 28/02/2021