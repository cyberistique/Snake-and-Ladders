import random as rd
from prettytable import PrettyTable
table = PrettyTable()
from turns import turn

class player:
    def __init__(self, name,pos):
        self.name = name
        self.pos = pos
            
player_data = []
Winners = []
stat = True

def main():
    n = int(input("enter the number of players: "))
    if n == 1:
        print("There cant be just one player... Try Again")
        main()
    for i in range(n):
        j = input("enter your name:")
        player_data.append(player(j,0))
    print("loading...")
    game()

def victory(N):
   player_data.remove(N)
   Winners.append(N)
   print(f" CONGO! {N.name} has completed the game... {N.name} is at {Winners.index(N)+1}th position")
   
def game():
    global stat
    print("""
........................
game is starting......
order of game is:""")
    for i in player_data:
        print(player_data.index(i)+1,".",i.name)
    while stat:
        for i in player_data:
            if len(player_data) == 1:
                stat = False
                table.field_names = ["Position", "Player"]
                for j in Winners:
                    table.add_row([Winners.index(j)+1,j.name])
                table.add_row([len(Winners)+1,i.name])
                print(table)
                print(f"WINNER: {Winners[0].name}    LOSER : {i.name}")
                print("THANKS FOR PLAYING")
                k = input("enter any key to EXIT")
            else:
                if i.pos == 100:
                    victory(i)
                else:
                    turn(i)
        
main()

