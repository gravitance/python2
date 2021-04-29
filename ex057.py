'''
EX 57 : IS IT A LEAP YEAR?

Most years have 365 days. However, the time required for the Earth to orbit the Sun
is actually slightly more than that. As a result, an extra day, February 29, is included
in some years to correct for this difference. Such years are referred to as leap years.
The rules for determining whether or not a year is a leap year follow:

• Any year that is divisible by 400 is a leap year.
• Of the remaining years, any year that is divisible by 100 is not a leap year.
• Of the remaining years, any year that is divisible by 4 is a leap year.
• All other years are not leap years.

Write a program that reads a year from the user and displays a message indicating
whether or not it is a leap year.

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

year = int(input("Enter a year: "))
isLeap = leap(year)

if isLeap == True:
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")