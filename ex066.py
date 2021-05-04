'''

EX 66 : COMPUTE A GRADE POINT AVERAGE

Exercise 51 included a table that shows the conversion from letter grades to grade
points at a particular academic institution.

In this exercise you will compute the grade point average of an arbitrary number of
letter grades entered by the user. The user will enter a blank line to indicate that
all of the grades have been provided. 

For example, if the user enters A, followed by C+, followed by B, followed by a blank
line then your program should report a grade point average of 3.1.

You may find your solution to Exercise 51 helpful when completing this exercise.

Your program does not need to do any error checking. It can assume that each value
entered by the user will always be a valid letter grade or a blank line.

'''

all_points = []

letter = input("Enter a letter grade: ")

if letter == '':
    print("Average must include at least 1 entry.")

else:
    while letter != '':

        if letter == 'A+' or letter == 'A':
            point = 4.0

        elif letter == 'A-':
            point = 3.7

        elif letter == 'B+':
            point = 3.3

        elif letter == 'B':
            point = 3.0

        elif letter == 'B-':
            point = 2.7

        elif letter == 'C+':
            point = 2.3

        elif letter == 'C':
            point = 2.0

        elif letter == 'C-':
            point = 1.7

        elif letter == 'D+':
            point = 1.3

        elif letter == 'D':
            point = 1.0

        else:
            point = 0
        
        all_points.append(point)
        letter = input("Enter a letter grade (blank to stop): ")
    
    gpa = sum(all_points) / len(all_points)
    print(f'Average GPA: {gpa:.2f}')