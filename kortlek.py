#!/usr/bin/env python3 
import string
import random
import re
import copy
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
    temp_deck = copy.deepcopy(deck)
    key = ""

    while (len(key) != length):
        move_card(temp_deck.index((1,0)), temp_deck.index((1,0)) + 1, temp_deck)
        move_card(temp_deck.index((2,0)), temp_deck.index((2,0)) + 2, temp_deck)
        

        joker1 = min(temp_deck.index((1,0)),temp_deck.index((2,0)))
        joker2 = max(temp_deck.index((1,0)),temp_deck.index((2,0)))

        A = temp_deck[:joker1]
        B = temp_deck[joker1:joker2 + 1]
        C = temp_deck[joker2+1:]
       # print(A,B,C)
        temp_deck = C + B + A
       # print(temp_deck)
        for i in range(value[temp_deck[len(temp_deck) - 1]]): #loopar från i till värdet av sista kortet
            temp_deck.insert(len(temp_deck) - 2, temp_deck.pop(0)) #lägger översta kortet näst längst ner
            
        if value[temp_deck[0]] == 27: #ifall en joker är längst upp så börjar vi om loopen igen
            pass
        else:
            key += string.ascii_uppercase[value[temp_deck[0]] - 1] #lägger till bokstav från A-Z beroende på värdet av första kortet i deck

    return key
    
def solitaire_encrypt(msg, deck, value):
    charvalue = {}
    numbervalue = {}
    msg_list = []
    key_list = []
    temp_list = []
    result_list = []
    msg = msg.upper()
    regexp = re.compile('[A-Z]') #tar endast ut tecken A-Z
    match = regexp.findall(msg) #kollar tecken för tecken och lägger in i en lista
    if match:
        msg = ''.join(match) # gör om listan till en sträng, onödigt?
    else:
        print("nope")
    key = solitaire_keystream(len(match), deck, value) # genererar nyckel med samma längd som meddelandet
    
    for i in string.ascii_uppercase: #loopar A-Z
        charvalue[i] = string.ascii_uppercase.index(i) + 1 #skapar en dict för att konvertera från bokstäver till siffror
    
    for i in msg:
        msg_list.append(charvalue[i]) #konverterar A-Z till siffror från meddelandet

    for i in key:
        key_list.append(charvalue[i]) #konverterar A-Z till sifrror från nyckeln
    
    for i in range(len(key)):
        number = msg_list[i] + key_list[i] #adderar de konverterade bokstäverna från key & msg
        if number > 26: #om resultatet är över 26 så tar vi bort 26
            number = number - 26
        temp_list.append(number) 
    
    for i in range(1,27):
        numbervalue[i] = string.ascii_uppercase[i - 1] #skapar en dict för att konvertera från siffror till bokstäver
    
    for i in temp_list:
        result_list.append(numbervalue[i]) #konverterar summan från föregående loop till bokstäver igen
    #print(result_list)
    #print(temp_list)
    #print(numbervalue)
    #print(msg)
    #print(msg_list)
    #print(key)
    #print(key_list)
    return ''.join(result_list)

def solitaire_decrypt(msg, deck, value):
    msg = msg.upper()
    charvalue = {}
    msg_list = []
    key_list = []
    temp_list = []
    result_list = []
    numbervalue = {}
    for i in string.ascii_uppercase: 
        charvalue[i] = string.ascii_uppercase.index(i) + 1 #skapar dict för att konvertera, behöver en funktion för detta
    for i in msg:
        msg_list.append(charvalue[i])
    key = solitaire_keystream(len(msg), deck, value)

    for i in key:
        key_list.append(charvalue[i])
    
    for i in range(len(key)):
        number = msg_list[i] - key_list[i] #subtraherar bokstäverna
        if number < 0:
            number = number + 26
        temp_list.append(number)

    for i in range(1,27):
        numbervalue[i] = string.ascii_uppercase[i - 1]

    for i in temp_list:
        result_list.append(numbervalue[i])

    return ''.join(result_list)
