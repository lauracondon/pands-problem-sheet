# collatz.py
# A program that asks the user to input any positive integer 
# and outputs the successive values of the following calculation.
# At each step it calculates the next value by taking the current value. 
# If it is even it divides it by two.
# If it is odd, it multiplies it by three and adds one.
# When the value is equal to one, the program ends. 
# Author: Laura Condon

# asks the user for their input and stores it as variable named 'value'
value = int(input("Please enter a positive integer: "))

# displays an error message if a negative integer is entered
if value <= 0:
    print("Sorry that is an invalid input. Try again with a postive integer.")

# initialises the while loop - will only work if user enters a postive integer
while value > 0 :
 # if the value is even
 if value % 2 == 0:
    print(value)
 # changes condition variable by dividing it by two, stores it as an integer
    value = value//2

 # if the value is odd and it does not equal one
 if value % 2 != 0 and value != 1:
    print(value)
 # changes condition variable by multiplying it by three, then adding one
    value = (value*3) + 1

 # if the value is equal to one
 elif value == 1:
    print(value)
 # value is now equal to 0 and the loop ends as a result
    value = (value - 1)

    