# weekday.py
# This program determines what day of the week it is and prints a related message
# Author: Laura Condon

# Import the datetime module 
from datetime import date
# Determine what the date is and store it as variable 'today'
today = date.today()
# Determine what day it is and stores it as variable 'whatDay'
whatDay = today.weekday()
# The days of the week are expressed numerically (so 0 = Monday, 1 = Tuesday etc.). 
# Ergo, if whatDay is less than five it means it's a weekday.
if whatDay < 5:
    print("Yes, unfortunately today is a weekday.")
# Otherwise, it's the weekend
else:
    print("It is the weekend, yay!")