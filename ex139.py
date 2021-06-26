'''

EX 139 : CHECKING FOR A WINNING CARD

A winning Bingo card contains a line of 5 numbers that have all been called. Players
normally mark the numbers that have been called by crossing them out or marking
them with a Bingo dauber. In our implementation we will mark that a number has
been called by replacing it with a 0 in the Bingo card dictionary.

Write a function that takes a dictionary representing a Bingo card as its only
parameter. If the card contains a line of five zeros (vertical, horizontal or diagonal)
then your function should return True, indicating that the card has won. Otherwise
the function should return False.

Create a main program that demonstrates your function by creating several Bingo
cards, displaying them, and indicating whether or not they contain a winning line.
You should demonstrate your function with at least one card with a horizontal line,
at least one card with a vertical line, at least one card with a diagonal line, and at
least one card that has some numbers crossed out but does not contain a winning line.
You will probably want to import your solution to Exercise 138 when completing
this exercise.

Hint: Because there are no negative numbers on a Bingo card, finding a line
of 5 zeros is the same problem as finding a line of 5 entries that sum to zero.
You may find the summation problem easier to solve.

'''

from ex138 import bingocard, displaycard

def check(card):

    # check verticals

    for column in card:
        if sum(card[column]) == 0:
            return True
    
    # check horizontals

    for i in range(5):
        row = 0
        for column in card:
            col = card[column]
            row += col[i]
        
        if row == 0:
            return True
    
    # check l-r diagonal

    right = card["B"][0] + card["I"][1] + card["N"][2] + card["G"][3] + card["O"][4]
    if right == 0:
        return True
    
    # check r-l diagonal

    left = card["B"][4] + card["I"][3] + card["N"][2] + card["G"][1] + card["O"][0]
    if left == 0:
        return True
    
    return False

def main():
    vert = {'B': [10, 3, 1, 5, 12], 'I': [0,0,0,0,0], 'N': [34, 41, 40, 32, 38], 'G': [57, 54, 59, 50, 48], 'O': [74, 66, 71, 65, 72]}
    hor = {'B': [10, 3, 1, 0, 12], 'I': [29, 24, 26, 0, 28], 'N': [34, 41, 40, 0, 38], 'G': [57, 54, 59, 0, 48], 'O': [74, 66, 71, 0, 72]}
    rightd = {'B': [0, 3, 1, 5, 12], 'I': [29, 0, 26, 18, 28], 'N': [34, 41, 0, 32, 38], 'G': [57, 54, 39, 0, 48], 'O': [74, 66, 71, 65, 0]}
    leftd = {'B': [10, 3, 1, 5, 0], 'I': [29, 24, 26, 0, 28], 'N': [34, 41, 0, 32, 38], 'G': [57, 0, 59, 50, 48], 'O': [0, 66, 71, 65, 72]}
    nowin = {'B': [10, 3, 1, 5, 12], 'I': [29, 24, 26, 18, 28], 'N': [34, 41, 40, 32, 38], 'G': [57, 54, 59, 50, 48], 'O': [74, 66, 71, 65, 72]}

    displaycard(vert)
    print(f"is it a winning card: {check(vert)}")
    print()

    displaycard(hor)
    print(f"is it a winning card: {check(hor)}")
    print()

    displaycard(rightd)
    print(f"is it a winning card: {check(rightd)}")
    print()

    displaycard(leftd)
    print(f"is it a winning card: {check(leftd)}")
    print()

    displaycard(nowin)
    print(f"is it a winning card: {check(nowin)}")
    print()

if __name__ == "__main__":
    main()