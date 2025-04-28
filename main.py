import random as rd
from prettytable import PrettyTable
table = PrettyTable()
from turns import turn

# made a player class with name and position attributes
class player:
    def __init__(self, name,pos):
        self.name = name
        self.pos = pos

# Empty lists that will hold the player class objects
player_data = []
Winners = []
stat = True # Used to stop game

# To make entry of players and append their class object in player_data
def main():
    n = int(input("enter the number of players: "))
    if n == 1: #for incase the user inputs '1'
        print("There cant be just one player... Try Again")
        main()
    for i in range(n):
        j = input("enter your name:")
        player_data.append(player(j,0)) # player object made and put in player_data with default position = 0
    print("loading...")
    game() # game function called

def victory(N): # for when a player reaches 100
   player_data.remove(N) #player removed from player_ data and moved to Winners to stop their turns
   Winners.append(N)
   print(f" CONGO! {N.name} has completed the game... {N.name} is at {Winners.index(N)+1}th position") # Announcement
   
def game():
    global stat #stat function True at the start
    print("""
........................
game is starting......
order of game is:""")
    for i in player_data: #prints the names of the players
        print(player_data.index(i)+1,".",i.name)
    while stat: # True while loop till stat is False
        for i in player_data: # player data is looped and turn takes place one by one
            if len(player_data) == 1: #For when just one player is left at the end and all others have reached 100
                stat = False # while loop stops
                table.field_names = ["Position", "Player"] # for the positions table
                for j in Winners:
                    table.add_row([Winners.index(j)+1,j.name])
                table.add_row([len(Winners)+1,i.name]) # loser is added to the end of the table
                print(table)
                print(f"WINNER: {Winners[0].name}    LOSER : {i.name}")
                print("THANKS FOR PLAYING")
                k = input("enter any key to EXIT") # End of game
            else: #when more than one player is left
                if i.pos == 100: # checks if 100 has been reached, if true victory function is called
                    victory(i)
                else:
                    turn(i) #normal circumstance- turn is called (in turns.py file)
        
main()

