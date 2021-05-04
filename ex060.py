'''

EX 60 : ROULETTE PAYOUTS

A roulette wheel has 38 spaces on it. Of these spaces, 18 are black, 18 are red, and two
are green. The green spaces are numbered 0 and 00. The red spaces are numbered
1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34 and 36. The remaining integers
between 1 and 36 are used to number the black spaces.

Many different bets can be placed in roulette. We will only consider the following subset of them in this exercise:

• Single number (1 to 36, 0, or 00)
• Red versus Black
• Odd versus Even (Note that 0 and 00 do not pay out for even)
• 1 to 18 versus 19 to 36

Write a program that simulates a spin of a roulette wheel by using Python’s random number generator. Display the number
that was selected and all of the bets that must be payed. For example, if 13 is selected then your program should display:

The spin resulted in 13...
Pay 13
Pay Black
Pay Odd
Pay 1 to 18

If the simulation results in 0 or 00 then your program should display Pay 0 or Pay 00 without any further output.

'''

import random

green = [0, 37]
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]

simulate_spin = random.randint(0, 37)

if simulate_spin in green:
    if simulate_spin == 37:
        simulate_spin = '00'
    print("The spin resulted in", simulate_spin, "...")
    print("Pay", simulate_spin)

else:
    print("The spin resulted in", simulate_spin, "...")
    print("Pay", simulate_spin)
    if simulate_spin in red:
        print("Pay Red")
    else:
        print("Pay Black")
    
    if (simulate_spin % 2 == 0):
        print("Pay Even")
    else:
        print("Pay Odd")
    
    if (simulate_spin < 19):
        print("Pay 1 to 18")
    else:
        print("Pay 19 to 36")