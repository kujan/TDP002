#!/usr/bin/env python3 

import random
import math
print("hej")
def create_deck():
    deck = []
    for v in range(1,14):
        for c in range(1,5):
            deck.append((v, c))
    return(deck)

def get_value(card):
    value = dict(ace=1,two=2,three=3,four=4,five=5,six=6,seven=7,eight=8,nine=9,ten=10,knight=11,queen=12,king=13)
    string = card.split('_')
    return value.get(string.pop(0))

def get_suit(card):
    suit = dict(hearts=1,spades=2,diamonds=3,clubs=4)
    string = card.split('_')
    return suit.get(string.pop(2))

def display_card(card):
    print(str(get_value(card)) + " of " + card.split('_').pop(2))

def shuffle_deck(deck):
    deck = create_deck()
    for x in range(300):
        num  = random.randint(0,51)
        deck.append(deck.pop(num))
    print(deck)
    for x in range(26):
        deck.append(deck.pop(0))
    print(deck)

def move_card(old, new):
    deck = create_deck()
    return deck.insert(new, (deck.pop(old)))
