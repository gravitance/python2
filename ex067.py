'''

EX 67 : ADMISSION PRICE

A particular zoo determines the price of admission based on the age of the guest.
Guests 2 years of age and less are admitted without charge. Children between 3 and
12 years of age cost $14.00. Seniors aged 65 years and over cost $18.00. Admission
for all other guests is $23.00.

Create a program that begins by reading the ages of all of the guests in a group
from the user, with one age entered on each line. The user will enter a blank line to
indicate that there are no more guests in the group. Then your program should display
the admission cost for the group with an appropriate message. The cost should be
displayed using two decimal places.

'''

guests = []
cost = 0
age = input("Enter the age of guest: ")

if age == '':
    print("There must be at least 1 guest.")

else:
    while age != '':
        age = int(age)
        guests.append(age)
        age = input("Enter the age of guest (blank to stop): ")
    
    for guest in guests:
        if guest <= 2:
            cost += 0
        elif (guest > 2 and guest < 12):
            cost += 14
        elif guest >= 65:
            cost += 18
        else:
            cost += 23
    
    print(f'Total cost: $ {cost:.2f}')