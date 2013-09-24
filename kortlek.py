#!/usr/bin/env python3 
import string
import random
def create_deck():
    value = {}
    deck = []
    jokera = create_card(1,0,deck)
    jokerb = create_card(2,0,deck)
    for v in range(1,14):
        for c in range(1,3):
            deck.append((v, c))
            value = define_cards(deck)
    shuffle_deck(deck)
    return deck, value

def create_card(v,c,deck):
    deck.append((v,c))

def display_card(card):
    print(str(get_value(card)) + " of " + card.split('_').pop(2))

def shuffle_deck(deck):
    random.shuffle(deck)
    for x in range(int(len(deck) / 2)):
        deck.append(deck.pop(0))

def move_card(old, new, deck):
    if deck[old] == (1,0):
        if old == 27:
             deck.insert(1,(deck.pop(old)))
        else:
            
            deck.insert(new, (deck.pop(old)))
    elif deck[old] == (2,0):
        if old == 27:
            deck.insert(2, (deck.pop(old)))
        elif old == 26:
            deck.insert(1, (deck.pop(old)))
        else:
            deck.insert(new, (deck.pop(old)))
    else:
        deck.insert(new, (deck.pop(old)))
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

def solitaire_keystream(length, deck, value):
    key = ""
    while (len(key) != length):
        move_card(deck.index((1,0)), deck.index((1,0)) + 1, deck)
        move_card(deck.index((2,0)), deck.index((2,0)) + 2, deck)


        joker1 = min(deck.index((1,0)),deck.index((2,0)))
        joker2 = max(deck.index((1,0)),deck.index((2,0)))

        A = deck[:joker1]
        B = deck[joker1:joker2 + 1]
        C = deck[joker2+1:]

        deck = C + B + A
    
        for i in range(value[deck[len(deck) - 1]]): #loopar från i till värdet av sista kortet
            deck.insert(len(deck) - 2, deck.pop(0)) #lägger översta kortet näst längst ner
            
    
        print(deck[0]) #debug
        if value[deck[0]] == 27: #ifall en joker är längst upp så börjar vi om loopen igen
            pass
        else:
            key += string.ascii_uppercase[value[deck[0]]] #lägger till bokstav från A-Z beroende på värdet av första kortet i deck

    return key
