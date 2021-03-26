# bmi.py
# This program calculates the user's Body Mass Index (BMI)
# author: Laura Condon

# try/except checks if user's input is an integer and delivers error message if not
try:
    
# prompts the user to enter their weight and height then converts it from a string to an integer. 
    weight = int(input("Please enter your weight in kilograms: "))
    height = int(input("Please enter your height in centimetres: "))

# calculates the user's BMI and stores it in the variable 'bmi' 
    bmi = weight/(height/100)**2

# prints the user's BMI
# converts the variable to a string and rounds it to two decimal places 
    print("Your BMI is " + str(round(bmi,2)))

# specifies error to be detected and delivers error message to the user if found
except ValueError:
    print("Invalid Input. Please enter numbers only")