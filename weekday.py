# weekday.py
# This program determines what day of the week it is 
# and prints a related message
# Author: Laura Condon

# import the datetime module 
from datetime import date
# determines what today's date is [1]
# and stores it as variable 'today'
today = date.today() 
# determines what day it is 
# and stores it as variable 'what_day'
what_day = today.weekday() 
# the days of the week are expressed numerically 
# (so 0 == Monday, 1 == Tuesday etc.) [2]
# ergo, if what_day is less than five it means it's a weekday.
if what_day < 5:
    print("Yes, unfortunately today is a weekday.")
# otherwise, it's the weekend
else:
    print("It is the weekend, yay!")

# References
# [1] https://www.programiz.com/python-programming/datetime (accessed 19/02/2021)
# [2] https://pythontic.com/datetime/date/weekday (accessed 19/02/2021)