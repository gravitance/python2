'''

EX 45 : WHAT COLOUR IS THAT SQUARE

Positions on a chess board are identified by a letter and a number. The letter identifies
the column, while the number identifies the row, as shown below:

Write a program that reads a position from the user. Use an if statement to determine if the column begins with a black square or a white square. Then use modular
arithmetic to report the color of the square in that row. For example, if the user enters
a1 then your program should report that the square is black. If the user enters d5
then your program should report that the square is white. Your program may assume
that a valid position will always be entered. It does not need to perform any error
checking.

'''

position = input("Enter a board position: ")

col = position[0]
row = int(position[1])

if col in "aceg":
    if row % 2 == 0:
        print(f'{position} is a white square.')
    else:
        print(f'{position} is a black square.')

else:
    if row % 2 == 0:
        print(f'{position} is a black square.')
    else:
        print(f'{position} is a white square.')