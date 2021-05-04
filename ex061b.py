'''

EX 61B : AVERAGE (VARIABLES)

In this exercise you will create a program that computes the average of a collection
of values entered by the user. The user will enter 0 as a sentinel value to indicate
that no further values will be provided. Your program should display an appropriate
error message if the first value entered by the user is 0.

Hint: Because the 0 marks the end of the input it should not be included in the
average.

'''

total, count = 0, 0
print("The average of the collection will be calculated.")
to_add = int(input("Enter a value to add (enter 0 to stop): "))

if to_add == 0:
    print("Collection must have at least 1 value.")

else:
    while to_add != 0:
        total += to_add
        count += 1
        to_add = int(input("Enter a value to add (enter 0 to stop): "))

    print(total, "", count)
    average = total/count
    print("The average of the collection is:", average)