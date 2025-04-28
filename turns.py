import random as rd
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

def turn(n): 
    k = input(f" {n.name}'s turn... enter any key to continue")
    l = rd.randint(1,6)
    if n.pos == 0:
        if l == 6 or l == 1:
            n.pos = 1
            print(f" YOU GOT A {l}!! You left the house... now at 1")
        else:
            print(f" Dice rolled a {l} ... still at home")
    elif n.pos > 94 and n.pos != 100 and l> (100 - n.pos):
            print(f"Nope you need {100-n.pos} or lower to continue")
    else:
        n.pos += l
        print(f"Dice rolled a {l} ... now at {n.pos}")
    if n.pos in snake.keys():
        print(f"Oops .. YOU WERE BITTEN BY A SNAKE AT {n.pos}, now at {snake[n.pos]}")
        n.pos = snake[n.pos]
    if n.pos in ladder.keys():
        print(f"AT {n.pos}, now at {ladder[n.pos]}")
        n.pos = ladder[n.pos]


