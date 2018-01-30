from time import time
import random
from card_generator import set_deck_creator

deck = set_deck_creator()


# returns a list of n random cards from a list of cards.
def deal_n_cards(deck, n):
    return random.sample(deck, 12)


# given a list of 3 cards, returns wether or not they form a set.
def cards_set_bool(cards):
    set = True
    for char in range(len(cards[0])):  # number of characterstics
        if cards[0][char] == cards[1][char]:
            set = cards[0][char] == cards[2][char]
        else:
            set = (cards[2][char] != cards[0][char] 
                   and cards[2][char] != cards[1][char])
        if not set:
            return False
    return True


true_set = [[1, 2, 0, 1], [1, 1, 1, 1], [1, 0, 2, 1]]
true_set1 = [[1, 0, 0, 1], [1, 0, 1, 1], [1, 0, 2, 1]]
assert cards_set_bool(true_set) is True
assert cards_set_bool(true_set1) is True


# given a list of 3 cards, return if there are any duplicates
def cards_unique(cards):
    string_cards = []

    def stringify_card(card):
        return "".join(str(x) for x in card)
    for card in cards:
        string_cards.append(stringify_card(card))
    return len(string_cards) == len(set(string_cards))


unique_set = [[1, 0, 0, 1], [1, 0, 1, 1], [1, 0, 2, 1]]
non_unique_set = [[1, 0, 0, 1], [1, 0, 0, 1], [1, 0, 2, 1]]
non_unique_set1 = [[1, 0, 0, 1], [1, 0, 0, 1], [1, 0, 0, 1]]
assert cards_unique(unique_set) is True
assert cards_unique(non_unique_set) is False
assert cards_unique(non_unique_set1) is False


# finds all sets in given list of cards.
def find_set(cards):
    nums = 0
    for x in cards:
        for y in cards:
            for z in cards:
                if cards_unique([x, y, z]):
                    if cards_set_bool([x, y, z]):
                        # print([x, y, z])
                        nums += 1
    return nums

# the deck has 81 cards, so there are 81*80*1 possible sets
# for any two cards there will always be a unique third card
# that completes the set.
# assert (find_set(deck) == 6480) is True
# find_set(deal_n_cards(deck,12))


# time to find all sets 100 groups of 12 cards, 10 times
def time_all_set_12():
    times = []
    for x in range(10):
        t0 = time()
        for y in range(100):
            find_set(deal_n_cards(deck, 12))
        t1 = time()
        times.append(t1-t0)
    print(sum(times)/len(times))


# time_all_set_12()

def time_all_sets_deck():
    times = []
    for x in range(5):
        random.shuffle(deck)
        t0 = time()
        find_set(deck)
        t1 = time()
        times.append(t1-t0)
    print(sum(times) / len(times))


# time_all_sets_deck()
