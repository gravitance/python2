'''

EX 61 : AVERAGE (LIST, WHILE TRUE)

In this exercise you will create a program that computes the average of a collection
of values entered by the user. The user will enter 0 as a sentinel value to indicate
that no further values will be provided. Your program should display an appropriate
error message if the first value entered by the user is 0.

Hint: Because the 0 marks the end of the input it should not be included in the
average.

'''

values = []
print("The average of the collection will be calculated.")
while True:
    to_add = int(input("Enter a value to add (enter 0 to stop): "))
    if (len(values) == 0) and to_add == 0:
        print("Collection must have at least 1 value.")
    elif to_add == 0:
        break
    else:
        values.append(to_add)

print(values)
values_average = sum(values)/len(values)
print("The average of the collection is:", values_average)