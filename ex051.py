'''

EX 51 : LETTER GRADE TO GRADE POINTS

At a particular university, letter grades are mapped to grade points in the following
manner:

Letter  Grade points
A+      4.0
A       4.0
A−      3.7
B+      3.3
B       3.0
B−      2.7
C+      2.3
C       2.0
C−      1.7
D+      1.3
D       1.0
F       0

Write a program that begins by reading a letter grade from the user. Then your
program should compute and display the equivalent number of grade points. Ensure
that your program generates an appropriate error message if the user enters an invalid
letter grade.

'''

letter = input("Enter a letter grade: ")

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

elif letter == 'F':
    point = 0

else:
    point = -1
    print("Invalid letter grade.")

if point != -1:
    print(f'Grade point: {point}')