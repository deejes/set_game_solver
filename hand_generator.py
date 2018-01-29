from card_generator import set_deck_creator
import random

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


# given a list of 3 cards, return if they are unique
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


# finds a set in given list of cards.
def find_set(cards):
    for x in cards:
        for y in cards:
            for y in cards:
                if len(x) > len(set(x)):
                    pass



