#!/usr/bin/env python3 

import random
print("hej")
def create_deck():
    value = {}
    deck = []
    jokera = create_card(1,0,deck)
    jokerb = create_card(2,0,deck)
    for v in range(1,14):
        for c in range(1,3):
            deck.append((v, c))
            value = define_cards(deck)
    return deck, value

def create_card(v,c,deck):
    deck.append((v,c))

def display_card(card):
    print(str(get_value(card)) + " of " + card.split('_').pop(2))

def shuffle_deck(deck):
    random.shuffle(deck)
    print(deck)
    for x in range(int(len(deck) / 2)):
        deck.append(deck.pop(0))
    print(deck)

def move_card(old, new, deck):
    deck.insert(new, (deck.pop(old)))
    print(deck)

def define_cards(deck):
    deck.sort(key=lambda tup: tup[1])
    value = {}
    for x in range(len(deck)):
        if deck[x][1] == 0:
            value[deck[x]] = 27
        else:
            value[deck[x]] = x + -1
        
    return value

def remove_card(pos, deck):
    deck.pop(pos)
