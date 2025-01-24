# A.0.7: Deal the cards (function and class) Mandatory - 3pts
# In many card games, each player is dealt a specific number of cards after the deck has been shuffled.
# Write a function, deal, which takes the number of hands, the number of cards per hand, and a deck of cards as its
# three parameters. Your function should return a list containing all of the hands that were dealt. Each hand will be
# represented as a list of cards. When dealing with the hands, your function should modify the deck of cards passed
# to it as a parameter, removing each card from the deck as it is added to a player’s hand. When cards are dealt, it
# is customary to give each player a card before any player receives an additional card. Your function should follow
# this custom when constructing the hands for the players.

# When done with writing the above function, use your solution to A.0.6 to help you construct a main class
# that creates, shuffles, and deals a deck of cards.

import random as rnd
from A_0_6 import create_deck

class Cards:
    deck = []

    def __init__(self):
        self.deck = create_deck()
        self.shuffle_deck()


    # Fisher-yates algorithm, this time just shuffling the deck, not returning anything
    def shuffle_deck(self):
        last_index = len(self.deck) - 1
        while last_index >= 0:
            rand = rnd.randint(0, last_index)
            temp = self.deck[last_index]
            self.deck[last_index] = self.deck[rand]
            self.deck[rand] = temp
            last_index -= 1


    def deal(self, hands, card_num):
        all_hands = []
        for i in range(hands):
            hand = []
            for j in range(card_num):
                hand.append(self.deck.pop(rnd.randint(0, len(self.deck) - 1)))
            all_hands.append(hand)
        for k in range (len(all_hands)):
            hand = all_hands[k]
            print(f"Hand #{k+1}: {hand}")



def main():
    cards = Cards()
    cards.deal(3, 6)


if __name__ == '__main__':
    main()