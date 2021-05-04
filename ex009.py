'''

EX 9 : COMPOUND INTEREST

Pretend that you have just opened a new savings account that earns 4 percent interest
per year. The interest that you earn is paid at the end of the year, and is added
to the balance of the savings account. Write a program that begins by reading the
amount of money deposited into the account from the user. Then your program should
compute and display the amount in the savings account after 1, 2, and 3 years. Display
each amount so that it is rounded to 2 decimal places.

'''

deposit = float(input("Enter initial deposit: $ "))
year1 = deposit * ((1+0.04)**1)
year2 = deposit * ((1+0.04)**2)
year3 = deposit * ((1+0.04)**3)

print(f'Balance after 1 year: $ {year1:.2f}')
print(f'Balance after 2 years: $ {year2:.2f}')
print(f'Balance after 3 years: $ {year3:.2f}')