'''

EX 140 : PLAY BINGO

In this exercise you will write a program that simulates a game of Bingo for a single
card. Begin by generating a list of all of the valid Bingo calls (B1 through O75). Once
the list has been created you can randomize the order of its elements by calling the
shuffle function in the random module. Then your program should consume calls
out of the list, crossing out numbers on the card, until the card contains a crossed out
line (horizontal, vertical or diagonal). Simulate 1,000 games and report the minimum,
maximum and average number of calls that must be made before the card wins. Import
your solutions to Exercises 138 and 139 when completing this exercise

'''

from ex138 import bingocard, displaycard
from ex139 import check
from random import shuffle

def generate_calls():
    calls = []

    for i in range(1, 16):
        calls.append("B" + str(i))

    for i in range(16, 31):
        calls.append("I" + str(i))

    for i in range(31, 46):
        calls.append("N" + str(i))

    for i in range(46, 61):
        calls.append("G" + str(i))

    for i in range(61, 76):
        calls.append("O" + str(i))
    
    shuffle(calls)
    return calls

def main():

    num_of_games = 1000
    min_calls = 75
    max_calls = 0
    total_calls = 0

    for g in range(num_of_games):
        print("------------------------------------------------------------------------------------")
        print(f"GAME NUMBER {g+1}")
        print("------------------------------------------------------------------------------------\n")

        all_calls = generate_calls()
        card = bingocard()

        print("your bingo card is:\n")
        displaycard(card)
        
        win = False
        track = 0
        i = 1

        while i < 76 and win == False:

            call = all_calls.pop(0)

            col = call[0]
            number = int(call[1:])

            print(f"Call {i} is: {call}.")
            #print()

            for c in "BINGO":
                for n in card[c]:
                    if n == number:
                        card[c][card[c].index(n)] = 0
            
            track += 1
            i += 1
            #displaycard(card)

            if check(card) == True:
                win = True
                print("\nThe card has won!\n")
        
        displaycard(card)
        print(f"{track} calls were made.")

        total_calls += track

        if track < min_calls:
            min_calls = track
        
        if track > max_calls:
            max_calls = track
        
        print("\n------------------------------------------------------------------------------------")
        print(f"END OF GAME NUMBER {g+1}")
        print("------------------------------------------------------------------------------------\n")
    
    print(f"the maximum number of calls to win was: {max_calls}.")
    print(f"the minimum number of calls to win was: {min_calls}.")
    print(f"the average number of calls to win was: {round(total_calls/num_of_games)}.")

if __name__ == "__main__":
    main()