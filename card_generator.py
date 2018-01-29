# Each card has a number, color, shape, and fill.



# we could encode these all as numbers


#each deck has 81 cards, each unique. 



def set_deck_creator():
    deck = []
    for a in range(3):
        for b in range(3):
            for c in range(3):
                for d in range(3):
                    deck.append([a,b,c,d])
    # deck is a list containing 81 unique lists, each with 4 elements with values 0,1,2
    return deck


# just for fun, lets return each deck as it would appear graphically
count = ["one","two","three"]
fill = ["solid","striped","empty"]
colors = ["red","green","purple"]
shape = ["circle", "triangle", "squiggly"]
card_attributes = [count,fill,colors,shape]

def visual_deck_creator(deck):
    visual_deck = deck
    for card in visual_deck:
        for j,feature in enumerate(card):
           card[j] = card_attributes[j][feature]
    return visual_deck

visual_deck=visual_deck_creator(set_deck_creator())




