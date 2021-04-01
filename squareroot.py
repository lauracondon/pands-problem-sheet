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

# combined try/except with a while loop so that if user enters wrong input
# it will 'loop' and ask them for a positive number
while True:
    try:
        #requests input from the user
        num =  float(input("Please enter a positive number: "))
        # checks if number is positive using assertion
        assert num > 0 
    # if it's not a postive number, throws an assertion error and requests input again
    except AssertionError:
        print("That was a negative number. Please try again")
        continue
    # throws an error message if user enters a string and requests input again
    except ValueError:
        print("That was a string. Please try again")
        continue
    else:
        # calls the function sqrt
        sqrtNum = (sqrt(num))
        # prints the output rounded to one decimal place - then breaks out of the while loop
        print("The square root of " + str(num) + " is approx. " + str(round(sqrtNum,1)))
        break


