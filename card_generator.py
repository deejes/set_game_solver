# Each card has a number, color, shape, and fill.

colors = ["red","green","purple"]
count = [1,2,3]
shape = ["circle", "triangle", "squiggly"]
fill = ["solid","striped","empty"]


# we could encode these all as numbers


#each deck has 81 cards, each unique. 



def return_set_deck():
    range3 = [i for i in range(3)]
    deck = []
    for a in range(3):
        for b in range(3):
            for c in range(3):
                for d in range(3):
                    deck.append([a,b,c,d])

    # deck is a list containing 81 unique lists, each with 4 elements with values 0,1,2
    return deck

print ((return_set_deck()))
