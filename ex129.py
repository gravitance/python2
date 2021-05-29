'''

EX 129 : TWO DICE SIMULATION

In this exercise you will simulate 1,000 rolls of two dice. Begin by writing a function
that simulates rolling a pair of six-sided dice. Your function will not take any
parameters. It will return the total that was rolled on two dice as its only result.

Write a main program that uses your function to simulate rolling two six-sided
dice 1,000 times. As your program runs, it should count the number of times that each
total occurs. Then it should display a table that summarizes this data. Express the
frequency for each total as a percentage of the total number of rolls. Your program
should also display the percentage expected by probability theory for each total.
Sample output is shown below.

'''
from random import randint

def simulate_roll():
    d1 = randint(1,6)
    d2 = randint(1,6)
    total = d1 + d2
    return total

def main():

    theoretical = {2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36, 7: 6/36, 8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36}
    simulation = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}

    for i in range(1000):
        rolled = simulate_roll()
        simulation[rolled] = simulation[rolled] + 1
    
    print(f"total        simulated        expected")
    print(f"              percent          percent")

    for prob in simulation.keys():
        print(f"{prob}              {(simulation[prob]/1000)*100:.2f}             {theoretical[prob]*100:.2f}")

if __name__ == "__main__":
    main()