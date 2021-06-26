'''

EX 138 : CREATE A BINGO CARD

A Bingo card consists of 5 columns of 5 numbers. The columns are labeled with the
letters B, I, N, G and O. There are 15 numbers that can appear under each letter. In
particular, the numbers that can appear under the B range from 1 to 15, the numbers
that can appear under the I range from 16 to 30, the numbers that can appear under
the N range from 31 to 45, and so on.

Write a function that creates a random Bingo card and stores it in a dictionary. The
keys will be the letters B, I, N, G and O. The values will be the lists of five numbers
that appear under each letter. Write a second function that displays the Bingo card
with the columns labeled appropriately. Use these functions to write a program that
displays a random Bingo card. Ensure that the main program only runs when the file
containing your solution has not been imported into another program.

You may be aware that Bingo cards often have a “free” space in the middle of
the card. We won’t consider the free space in this exercise.

'''

def bingocard():

    from random import randrange
    card = {}

    start = 1
    end = 1 + 15

    for ch in ["B", "I", "N", "G", "O"]:
        card[ch] = []

        while len(card[ch]) < 5:
            num = randrange(start,end)
            if num not in card[ch]:
                card[ch].append(num)
        
        start += 15
        end += 15
    
    return card

def displaycard(card):
    print("B   I   N   G   O")
    print()

    for i in range(5):
        for ch in ["B", "I", "N", "G", "O"]:
            print(f'{card[ch][i]}   ', end="")
        print()
        print()

def main():
    card = bingocard()
    displaycard(card)

if __name__ == "__main__":
    main()

