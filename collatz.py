# collatz.py
# A program that asks the user to input any positive integer and outputs the successive values of the following calculation.
# At each step it calculates the next value by taking the current value. 
# If it is even it divides it by two.
# If it is odd, it multiplies it by three and adds one.
# When the value is equal to one, the program ends. 
# Author: Laura Condon

# asks the user for their input and stores it as variable named 'value'
value = int(input("Please enter a positive integer: "))
# initialises the while loop, ensures program only works if user enters a positive value
while value > 0 :
 # if the value is even
 if value % 2 == 0:
    print(value)
 # changes condition variable by dividing it by two, stores it as an integer
    value = int(value/2)
 # if the value is odd and it is greater than one
 if value % 2 != 0 and value > 1:
    print(value)
 # changes condition variable by multiplying it by three, then adding one
    value = (value*3)+1
 # if the value is equal to one
 elif value == 1:
    print(value)
 # ends the loop as value is no longer a positive integer - use break here instead possibly? 
    value = (value - 1)
    