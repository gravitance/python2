'''

EX 58 : NEXT DAY

Write a program that reads a date from the user and computes its immediate successor.
For example, if the user enters values that represent 2013-11-18 then your program
should display a message indicating that the day immediately after 2013-11-18 is
2013-11-19. If the user enters values that represent 2013-11-30 then the program
should indicate that the next day is 2013-12-01. If the user enters values that represent
2013-12-31 then the program should indicate that the next day is 2014-01-01. The
date will be entered in numeric form with three separate input statements; one for
the year, one for the month, and one for the day. Ensure that your program works
correctly for leap years.

'''

from ex057 import leap

if __name__ == "__main__":

    year = int(input("Enter a year (4 digit numeric): "))
    month = int(input("Enter a month (numeric): "))
    day = int(input("Enter a day (numeric): "))
    
    if month in [4, 6, 9, 11]:
        if day == 30:
            day = 1
            month += 1
        else:
            day += 1
    
    elif month == 2:

        if day == 28:

            isLeap = leap(year)
            if isLeap == True:
                day += 1
            else:
                day = 1
                month += 1
        
        elif day == 29:
            day = 1
            month += 1
        
        else:
            day += 1
    
    elif month == 12 and day == 31:
        year += 1
    
    else:

        if day == 31:
            day = 1
            month += 1
        
        else:
            day += 1

    print(f"the next day is: {year}-{month:02d}-{day:02d}.")