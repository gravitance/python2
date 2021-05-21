'''

EX 112 : BELOW AND ABOVE AVERAGE

Write a program that reads numbers from the user until a blank line is entered. Your
program should display the average of all of the values entered by the user. Then
the program should display all of the below average values, followed by all of the
average values (if any), followed by all of the above average values. An appropriate
label should be displayed before each list of values

'''

numlist = []
num = input("Enter a value: ")

if num == "":
    print("First entry cannot be blank.")

else:
    while num != "":
        num = float(num)
        numlist.append(num)
        num = input("Enter a value (blank to stop): ")

    average = sum(numlist)/len(numlist)
    below = []
    exact = []
    above = []

    for number in numlist:
        if number < average:
            below.append(number)
        elif number > average:
            above.append(number)
        else:
            exact.append(number)

    print(f"all numbers: {numlist}")
    print(f"average: {average}")
    print(f"numbers below average: {below}")
    if len(exact) > 0:
        print(f"numbers at average: {exact}")
    print(f"numbers above average: {above}")