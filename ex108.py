'''

EX 108 : NEGATIVES, ZEROS, POSITIVES

Create a program that reads integers from the user until a blank line is entered. Once
all of the integers have been read your program should display all of the negative
numbers, followed by all of the zeros, followed by all of the positive numbers. Within
each group the numbers should be displayed in the same order that they were entered
by the user. For example, if the user enters the values 3, -4, 1, 0, -1, 0, and -2 then
your program should output the values -4, -1, -2, 0, 0, 3, and 1. Your program
should display each value on its own line.

'''

negative = []
positive = []
zero_count = 0

number = input("Enter an integer: ")

if number == '':
    print("First entry cannot be blank.")

else:
    while number != '':
        if int(number) < 0:
            negative.append(number)
        elif int(number) == 0:
            zero_count = zero_count + 1
        else:
            positive.append(number)
        
        number = input("Enter an integer (blank to stop): ")

print()

for n in negative:
    print(n)

for z in range(zero_count):
    print(0)

for p in positive:
    print(p)