# A.0.6. Shuffle the cards! (function) Mandatory - 2pt

# A standard deck of playing cards contains 52 cards. Each card has one of four suits along with a value.
# The suits are normally spades, hearts, diamonds, and clubs while the values are 2 through 10, Jack, Queen, King
# and Ace. Each playing card can be represented using two characters. The first character is the value of the card,
# with the values 2 through 9 being represented directly. The characters “T”, “J”, “Q”, “K” and “A” are used to
# represent the values 10, Jack, Queen, King and Ace respectively. The second character is used to represent the
# suit of the card. It is normally a lowercase letter: “s” for spades, “h” for hearts, “d” for diamonds and “c” for
# clubs. The following table provides several examples of cards and their two-character representations.

# Begin by writing a function named createDeck. It will use loops to create a complete deck of cards by adding the
# suit to the number and storing the two-character abbreviations for all 52 cards in a list. Return the list of cards
# as the function’s only result. Your function will not take any parameters.
#
#  Write a second function named shuffle that randomizes the order of the cards in a list. The input of the function
#  should be the list contacting the deck of cards (52 items) that you have created in the previous function.
#  You can use the "random" library shuffle function. Alternatively, you can write your own shuffling function:  One
#  technique that can be used to shuffle the cards is to visit each element in the list and swap it with another
#  random element in the list. You must write your own loop for shuffling the cards. The output of the function should
#  be 2 lists: the deck of cards before shuffling and the deck of cards after shuffling.

import random as rnd

nums = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
signs = ['s', 'c', 'd', 'h']


def main():
    deck, shuffled_deck = shuffle_deck(create_deck())
    print(deck)
    print(shuffled_deck)


def create_deck():
    deck = []
    for num in nums:
        for sign in signs:
            card  = num + sign
            deck.append(card)
    return deck


# Fisher-yates algorithm, except I am adding values to the new deck instead of shuffling the same one
def shuffle_deck(deck):
    shuffled_deck = deck.copy()
    last_index = len(shuffled_deck) - 1
    while last_index >= 0:
        rand = rnd.randint(0, last_index)
        temp = shuffled_deck[last_index]
        shuffled_deck[last_index] = shuffled_deck[rand]
        shuffled_deck[rand] = temp
        last_index -= 1
    return deck, shuffled_deck


if __name__ == "__main__":
    main()