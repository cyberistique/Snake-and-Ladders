import random as rd
# dictionaries with postions of snakes and ladders
snake = {
         99:22,
         97:85,
         89:67,
         76:63,
         66:24,
         59:45,
         39:3,
         27:7,
         50:34,
         }
ladder = {
         23:87,
         66:77,
         55:65,
         28:72,
         50:67,
         21:42,
         8:30,
         4:14,
         2:22,
         }

def turn(n): #turn function - player object inputted
    k = input(f" {n.name}'s turn... enter any key to continue") # press enter to continue to next turn
    l = rd.randint(1,6) # Dice
    if n.pos == 0: #for when player at home, player only exits if dice returns 1 or 6
        if l == 6 or l == 1:
            n.pos = 1
            print(f" YOU GOT A {l}!! You left the house... now at 1") # Announcement
        else:
            print(f" Dice rolled a {l} ... still at home")
    elif n.pos > 94 and n.pos != 100 and l> (100 - n.pos): # when at final positions
            print(f"Nope you need {100-n.pos} or lower to continue")
    else: # Dice turn
        n.pos += l
        print(f"Dice rolled a {l} ... now at {n.pos}") # Announcement
    if n.pos in snake.keys(): # if position is that of one of the snakes
        print(f"Oops .. YOU WERE BITTEN BY A SNAKE AT {n.pos}, now at {snake[n.pos]}") # Announcement
        n.pos = snake[n.pos] # player moved
    if n.pos in ladder.keys(): # if position is that of one of the snakes
        print(f"AT {n.pos}, now at {ladder[n.pos]}") # Announcement
        n.pos = ladder[n.pos] # player moved


