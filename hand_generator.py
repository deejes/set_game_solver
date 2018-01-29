from card_generator import set_deck_creator
import random

deck = set_deck_creator()
#print(deck)


# returns a list of n random cards from a list of cards.
def deal_n_cards(deck,n):
     return random.sample(deck,12)

# given 3 cards, returns wether or not they form a set.
def cards_set_bool(cards):
    pass

# finds a set in given list of cards.
def find_set(cards):
    pass
