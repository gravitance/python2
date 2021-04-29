'''
EX 100 : DAYS IN A MONTH

Write a function that determines how many days there are in a particular month. Your
function will take two parameters: The month as an integer between 1 and 12, and
the year as a four digit integer. Ensure that your function reports the correct number
of days in February for leap years. Include a main program that reads a month and
year from the user and displays the number of days in that month. You may find your
solution to Exercise 57 helpful when solving this problem.

'''
def leap(year):
    isLeap = False
    if year % 400 == 0:
        isLeap = True
    else:
        if year % 100 == 0:
            isLeap = False
        else:
            if year % 4 == 0:
                isLeap = True
            else:
                isLeap = False
    
    return isLeap

def daysInMonth(month, year):

    days = 0
    days30 = [4,6,9,11]

    if month == 2:
        isLeap = leap(year)
        if isLeap == True:
            days = 29
        else:
            days = 28
    
    elif month in days30:
        days = 30
    
    else:
        days = 31

    return days

# ------------------

month = int(input("Enter a month: "))
year = int(input("Enter a year: "))
days = daysInMonth(month,year)
print("There are", days, "days.")