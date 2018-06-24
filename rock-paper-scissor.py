import random

'''
Rock paper scissor game 
'''

player1_input = int(input("Please Enter the selection \n1. Rock \n2. Paper \n3. Scissor\nEnter Here: "))

selection = ['Rock', 'Paper', 'Scissor']

player2_throw = random.choice(selection)

player1_point = int(0)
player2_point = int(0)
    


if player1_input == 1:
    player1_throw = 'Rock'
    
elif player1_input == 2:
    player1_throw = 'Paper'
    
elif player1_input == 3:
    player1_throw = 'Scissor'
    

else:
    print("Enter Corect Selection:\n1. Rock \n2. Paper \n3. Scissor\n")
    
    

if (player1_throw == 'Rock') and (player2_throw == 'Scissor'):
    player1_point += 1
    print("Player 1 Selected: ", player1_throw)
    print("Player 2 Selected: ", player2_throw)
    print("Player 1 Wins this game")
    
elif (player1_throw == 'Scissor') and (player2_throw == 'Paper'):
    player1_point += 1
    print("Player 1 Selected: ", player1_throw)
    print("Player 2 Selected: ", player2_throw)
    print("Player 1 Wins this game")
    
elif (player1_throw == 'Paper') and (player2_throw == 'Rock'):
    player1_point += 1
    print("Player 1 Selected: ", player1_throw)
    print("Player 2 Selected: ", player2_throw)
    print("Player 1 Wins this game")
    
elif (player2_throw == 'Paper') and (player1_throw == 'Rock'):
    player2_point += 1
    print("Player 1 Selected: ", player1_throw)
    print("Player 2 Selected: ", player2_throw)
    print("Player 2 Wins this game")
    
elif (player2_throw == 'Paper') and (player1_throw == 'Rock'):
    player2_point += 1
    print("Player 1 Selected: ", player1_throw)
    print("Player 2 Selected: ", player2_throw)
    print("Player 2 Wins this game")
    
elif (player2_throw == 'Paper') and (player1_throw == 'Rock'):
    player2_point += 1
    print("Player 1 Selected: ", player1_throw)
    print("Player 2 Selected: ", player2_throw)
    print("Player 2 Wins this game")

elif player1_throw == player2_throw:
    print("Player 1 Selected: ", player1_throw)
    print("Player 2 Selected: ", player2_throw)
    print("Game Tie No One Wins")
    
    
print("Player 1 Points: ", player1_point)
print("Player 2 Points: ", player2_point)




    


    
