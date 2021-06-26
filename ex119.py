'''

EX 119 : DEALING HANDS OF CARDS

In many card games each player is dealt a specific number of cards after the deck
has been shuffled. Write a function, deal, which takes the number of hands, the
number of cards per hand, and a deck of cards as its three parameters. Your function
should return a list containing all of the hands that were dealt. Each hand will be
represented as a list of cards.

When dealing the hands, your function should modify the deck of cards passed
to it as a parameter, removing each card from the deck as it is added to a player’s
hand. When cards are dealt, it is customary to give each player a card before any
player receives an additional card. Your function should follow this custom when
constructing the hands for the players.

Use your solution to Exercise 118 to help you construct a main program that
creates and shuffles a deck of cards, and then deals out four hands of five cards each.
Display all of the hands of cards, along with the cards remaining in the deck after
the hands have been dealt.

'''

from ex118 import createDeck, shuffle

def deal(hands, size, deck):

    if (hands*size) > len(deck):
        return [],[]
    
    else:

        from random import randrange

        dealing = []

        for i in range(hands):
            hand = []
            for card in range(size):
                random = randrange(0,len(deck))
                hand.append(deck.pop(random))
            dealing.append(hand)
        
        return dealing, deck

def main():

    deck = createDeck()
    print(f"the original card deck is: {deck}")
    
    print()
    
    shuffled = shuffle(deck)
    print(f"the shuffled deck is: {shuffled}")

    print()

    dealing, left = deal(4, 5, shuffled)
    print(f"the cards are dealt: {dealing}")
    print()
    print(f"the remaining cards are: {left}")

if __name__ == "__main__":
    main()