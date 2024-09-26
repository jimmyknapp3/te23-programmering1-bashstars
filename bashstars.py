from math import *
from random import randint

player1_hp = int(10)
player2_hp = int(10)
play = (True)
round = int(0)

while play == True:
    round += 1
    player1_roll = randint(1,6)
    player2_roll = randint(1,6)
    if player1_roll > player2_roll:
        player2_hp -= 1
        print(f"player 1 won the round with {player1_roll} over {player2_roll}")
    elif player2_roll > player1_roll:
        player1_hp -= 1
        print(f"player 2 won the round with {player2_roll} over {player2_roll} ")
    elif player2_roll == player1_roll:
        print("Draw")
    if player1_hp == int(0) or player2_hp == int(0):
        play = (False)
        print(f"player 1 have {player1_hp} hp")
        print(f"player 2 have {player2_hp} hp")
        print(f"{round} rounds")
    


