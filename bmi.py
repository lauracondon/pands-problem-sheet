# bmi.py
# This program calculates the user's Body Mass Index (BMI)
# Author: Laura Condon

# try/except checks if user's input is a number 
# delivers an error message if it is not [1]
try:

# prompts the user to enter their weight and height 
# then converts it from a string to a float
    weight = float(input("Please enter your weight in kilograms: "))
    height = float(input("Please enter your height in centimetres: "))

# calculates the user's BMI
# and stores it in the variable 'bmi' 
    bmi = weight/(height/100)**2

# prints the user's BMI
# converts the variable to a string
# and rounds it to two decimal places [2]
    print("Your BMI is " + str(round(bmi,2))) 

# specifies error to be detected 
# and delivers error message to the user if found
except ValueError:
    print("Invalid Input. Please enter numbers only")
    
# References 
# [1] https://docs.python.org/3/tutorial/errors.html (accessed 30/01/2021)
# [2] https://stackoverflow.com/questions/20457038/how-to-round-to-2-decimals-with-python