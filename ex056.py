'''

EX 56 : CELL PHONE BILL

A particular cell phone plan includes 50 minutes of air time and 50 text messages
for $15.00 a month. Each additional minute of air time costs $0.25, while additional
text messages cost $0.15 each. All cell phone bills include an additional charge of
$0.44 to support 911 call centers, and the entire bill (including the 911 charge) is
subject to 5 percent sales tax.

Write a program that reads the number of minutes and text messages used in a
month from the user. Display the base charge, additional minutes charge (if any),
additional text message charge (if any), the 911 fee, tax and total bill amount. Only
display the additional minute and text message charges if the user incurred costs in
these categories. Ensure that all of the charges are displayed using 2 decimal places.

'''

base = 15.00
fee = 0.44
add_minutes = 0
add_texts = 0

minutes = int(input("Call time in minutes this month: "))
texts = int(input("Texts sent this month: "))

if minutes > 50:
    add_minutes += (minutes-50)*0.25

if texts > 50:
    add_texts += (texts-50)*0.15

tax = (base + fee + add_minutes + add_texts) * 0.05
total = base + fee + add_minutes + add_texts + tax

print()
print(f"----------------------------------")
print(f"          CELL PHONE BILL         ")
print(f"----------------------------------")
print()
print(f"Base charge: ${base:.2f}")

if add_minutes > 0:
    print(f"Additional minutes charge: ${add_minutes:.2f}")
if add_texts > 0:
    print(f"Additional text message charge: ${add_texts:.2f}")

print(f"911 fee: ${fee:.2f}")
print(f"Sales tax: ${tax:.2f}")
print()
print(f"Total bill: ${total:.2f}")
print()
print(f"----------------------------------")

