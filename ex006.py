'''

EX 6 : TAX AND TIP

The program that you create for this exercise will begin by reading the cost of a meal
ordered at a restaurant from the user. Then your program will compute the tax and
tip for the meal. Use your local tax rate when computing the amount of tax owing.
Compute the tip as 18 percent of the meal amount (without the tax). The output from
your program should include the tax amount, the tip amount, and the grand total for
the meal including both the tax and the tip. Format the output so that all of the values
are displayed using two decimal places.

'''

cost = float(input("Cost of meal: $ "))
tax = 0.07 * cost
tip = 0.18 * cost
total = cost + tax + tip

print(f'Tax amount: $ {tax:.2f}')
print(f'Tip amount: $ {tip:.2f}')
print(f'Grand total: $ {total:.2f}')