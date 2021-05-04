'''

EX 103 : MAGIC DATES

A magic date is a date where the day multiplied by the month is equal to the two digit
year. For example, June 10, 1960 is a magic date because June is the sixth month, and
6 times 10 is 60, which is equal to the two digit year. Write a function that determines
whether or not a date is a magic date. Use your function to create a main program
that finds and displays all of the magic dates in the 20th century. You will probably
find your solution to Exercise 100 helpful when completing this exercise.

'''

# 20th century is from 1/1/1901 to 31/12/2000

def leap(year):                     # from exercise 57

    if year % 400 == 0:
        return True
    else:
        if year % 100 == 0:
            return False
        else:
            if year % 4 == 0:
                return True
            else:
                return False

def daysInMonth(month, year):       # from exercise 100

    days = 0
    days_30 = [4,6,9,11]

    if month == 2:
        is_leap = leap(year)
        if is_leap == True:
            days = 29
        else:
            days = 28
    
    elif month in days_30:
        days = 30
    
    else:
        days = 31

    return days

def magicDate(day, month, year):

    y = str(year)
    year = y[2:4]
    
    if day*month == int(year):
        return True
    else:
        return False 

print("All magic dates from 1/1/1901 to 31/12/2000:\n")

for year in range(1901,2001):
    for month in range(1,13):
        days = daysInMonth(month, year)
        for day in range(1,days+1):
            is_magic = magicDate(day,month,year)
            if is_magic == True:
                print(day, "/", month, "/", year)
