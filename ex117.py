'''

EX 117 : LINE OF BEST FIT

A line of best fit is a straight line that best approximates a collection of n data points.
In this exercise, we will assume that each point in the collection has an x coordinate
and a y coordinate. The symbols x¯ and y¯ are used to represent the average x value in
the collection and the average y value in the collection respectively. The line of best
fit is represented by the equation y = mx + b where m and b are calculated using
the following formulas:

blabla

Write a program that reads a collection of points from the user. The user will enter
the x part of the first coordinate on its own line, followed by the y part of the first
coordinate on its own line. Allow the user to continue entering coordinates, with the
x and y parts each entered on their own line, until your program reads a blank line for
the x coordinate. Display the formula for the line of best fit in the form y = mx + b
by replacing m and b with the values you calculated using the preceding formulas.
For example, if the user inputs the coordinates (1, 1), (2, 2.1) and (3, 2.9) then your
program should display y = 0.95x + 0.1.

'''

from math import *

x = []
y = []

x_val = input("Enter x coordinate: ")

if x_val == '':
    print("There must be at least 2 coordinates.")

else:
    y_val = input("Enter y coordinate: ")
    x.append(float(x_val))
    y.append(float(y_val))
    x_val = input("Enter x coordinate: ")
    
    while x_val != '':
        if len(x) > 1:
            y_val = input("Enter y coordinate (blank to stop): ")
            x.append(float(x_val))
            y.append(float(y_val))
            x_val = input("Enter x coordinate (blank to stop): ")
        else:
            y_val = input("Enter y coordinate: ")
            x.append(float(x_val))
            y.append(float(y_val))
            x_val = input("Enter x coordinate (blank to stop): ")

    if len(x) < 2:
        print("There must be at least 2 coordinates.")

    else:
        print(x)
        print(y)

        sum_xy = 0
        sum_x2 = 0

        for i in range(len(x)):
            sum_xy += x[i] * y[i]
            sum_x2 += x[i]**2

        m = (sum_xy - (sum(x)*sum(y)/len(x)))/(sum_x2 - ((sum(x))**2/len(x)))

        b = (sum(y)/len(y)) - (m*(sum(x)/len(x)))

        print(f'y = {m:.2f}x + {b:.2f}')