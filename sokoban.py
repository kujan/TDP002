#!/usr/bin/env python3

def soko_display(level_list):
    items = {'wall': '#','crate': 'O', 'player': '@','storing_space': '.','crate_in_position': '*', 'player_in_storage': '+','floor': " "}
    level = []     
    y_max = max(level_list, key=lambda x: x[2])[2] + 1 #hittar det högsta y-värdet i listan walls 
    
    for rows in range(y_max): #Loopar igenom alla Y från 0 till y-max, där varje loop är en rad
        row = []
        for y in level_list: #går igenom varje element i listan walls
            if y[2] == rows: #om Y-värdet i elementet är lika med den nuvarande raden 
                row.append(y) #lägger till hela elementet i en lista för just den raden
        level.append(row) #när vi har hittat alla Y för en rad, så lägger vi in dem i level
    for row in level: #går igenom alla element för denna rad
        row.sort(key=lambda tup: tup[1]) #sorterar listan efter X-värdet i stigande ordning
        print_row = ""
        if row != []:
            #x_max = max(row, key=lambda x: x[1])[1] #vi hittar det högsta x-värdet
            x = 0
            for element in row: #går igenom alla element i row
                doLoop = True
                while doLoop: #denna loopen ser till att det blir mellanslag mellan alla element
                    if element[1] == x: #kollar om x i element är lika med den nuvarande platsen i raden
                        print_row += items[element[0]] #lägger till värdet i strängen
                        x = x + 1 #X bestämmer vilken position i raden vi befinner oss på just nu
                        doLoop = False #hittar vi ett element som ska skrivas ut på denna plats, så avslutar vi loopen
                                        
                    else:
                        x = x + 1
                        #doLoop = True         
                        print_row += " "#hittas inget element så skriver vi ut mellanslag tills vi hittar ett
                        
            print(print_row)
        else:
            print("")
    return 
        
def load_level(file):
    level = open(file, 'r')
    level_list = []
    items = {'#': 'wall', 'o': 'crate', '@': 'player', '.': 'storing_space', '*': 'crate_in_position', '+': 'player_in_storage'," ": 'floor'}
    for y_index,row in enumerate(level):
        for x_index,char in enumerate(row):
            if char not in " \n":
                row_list = [items[char], x_index ,y_index]
                level_list.append(row_list)
    return level_list
def player_can_move(move, level):
    #hitta player i listan
    #kolla vad som finns där move är
    #så länge det inte är en vägg, och crate_can_move är true så flyttas spelaren
    #annars returnar vi någon typ av fel
    player = find_player(level)
    #player = 11, 8
    if move == 'up':
        check_object = find_item_in_coord(player[1],player[2] - 1, level)
        if check_object != 'wall' and crate_can_move(move,level):
            level.pop(level.index(player))
            player = [player[0],player[1],player[2] - 1]
            level.append(player)
        else:
            print("False move!")       
            
    elif move == 'down':
        check_object = find_item_in_coord(player[1],player[2] + 1, level)
        if check_object != 'wall' and crate_can_move(move,level):
            level.pop(level.index(player))
            player = [player[0],player[1],player[2] + 1]
            level.append(player)
        else:
            print("False move!")
    elif move == 'left':
        check_object = find_item_in_coord(player[1] - 1,player[2], level)
        if check_object != 'wall' and crate_can_move(move,level):
            level.pop(level.index(player))
            player = [player[0],player[1] - 1,player[2]]
            level.append(player)
        else:
            print("False move!")
    elif move == 'right':
        check_object = find_item_in_coord(player[1] + 1,player[2], level)
        if check_object != 'wall' and crate_can_move(move,level):
            level.pop(level.index(player))
            player = [player[0],player[1] + 1,player[2]]
            level.append(player)

        else:
            print("False move")
    return soko_display(level)
    
def check_move(move, steps, level):

    player = find_player(level)
    #player = 11, 8
    if move == 'up':
        check_object = find_item_in_coord(player[1],player[2] - steps, level)
        print(player[1],player[2] - steps)
        if check_object not in 'wallcrate':
            return check_object

    elif move == 'down':
        check_object = find_item_in_coord(player[1],player[2] + steps, level)
        if check_object not in 'wallcrate':
            return check_object      

    elif move == 'left':
        check_object = find_item_in_coord(player[1] - steps,player[2], level)
        print(steps)
        if check_object not in 'wallcrate':
            return check_object
    elif move == 'right':
        check_object = find_item_in_coord(player[1] + steps,player[2], level)
        if check_object not in 'wallcrate':
            return check_object
    else:
        print("False move")
        return False
def crate_can_move(move, level):
    #hitta player
    #koll vad som finns på move
    #om det är en låda, kolla bakom den lådan vad som finns. Är det en vägg eller en låda, returna false
    #annars returnera true
    player = find_player(level)
    find_move = check_move(move, 1, level)
    if find_move == 'crate':
        print("BALLE")
        find_move = check_move(move,2, level)
        if find_move == True:
            print("BALOBAS")
            return True

        else:
            return False
    else:
        return True
    


def find_item_in_coord(x,y, level):
    for element in level:
        if element[1] == x and element[2] == y:
            print(element[0])
            return element[0]
        elif element[0] == None:
            return ""
        else:
            return 'ERROR'
        
def find_player(level):
    for element in level:
        if element[0] == 'player':
            return element
        
def create_stuff (items, x,y):
    stuff = {items: (x,y)}
    return stuff       
    
def create_wall(x,y):
    [['wall', 1,0], ['wall', 2, 0], ['wall', 2,1]]
    walls = []
    walls.append('wall')
    walls.append(x)
    walls.append(y)
    return walls

def create_player(x,y):
    player = []
    player.append(x)
    player.append(y)
    return player

def create_crates(x,y):
    crates = []
    crates.append(x,y)

def create_floor(x,y):
    print("hej")
def create_storing_space(x,y):
    print("hej")
