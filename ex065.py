'''

EX 65 : PERIMETER OF A POLYGON

Write a program that computes the perimeter of a polygon. Begin by reading the x
and y values for the first point on the perimeter of the polygon from the user. Then
continue reading pairs of x and y values until the user enters a blank line for the
x-coordinate. Each time you read an additional coordinate you should compute the
distance to the previous point and add it to the perimeter.

When a blank line is entered for the x-coordinate your program should add the distance from
the last point back to the first point to the perimeter. Then it should display the total perimeter.

Sample input and output is shown below, with user input shown in bold:

Enter the x part of the coordinate: 0
Enter the y part of the coordinate: 0
Enter the x part of the coordinate: (blank to quit): 1
Enter the y part of the coordinate: 0
Enter the x part of the coordinate: (blank to quit): 0
Enter the y part of the coordinate: 1
Enter the x part of the coordinate: (blank to quit):
The perimeter of that polygon is 3.414213562373095

'''

import math

x1 = float(input("Enter the x part of the coordinate: "))
y1 = float(input("Enter the y part of the coordinate: "))

temp_x = x1
temp_y = y1

perimeter = math.sqrt((x1-temp_x)**2 + (y1-temp_y)**2)

x = input("Enter the x part of the coordinate (blank to quit): ")
if x == '':
    perimeter = 0

else:
    while x != '':
        x = float(x)
        y = float(input("Enter the y part of the coordinate: "))
        length = math.sqrt((x-temp_x)**2 + (y-temp_y)**2)
        perimeter += length
        
        temp_x = x
        temp_y = y

        x = input("Enter the x part of the coordinate (blank to quit): ")
    
    perimeter += math.sqrt((temp_x-x1)**2 + (temp_y-y1)**2)

print(f'The perimeter of that polygon is {perimeter}.')