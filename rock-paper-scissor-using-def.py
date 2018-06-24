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
    
    

def compare(p1_throw, p1_point,p2_throw, p2_point):  
 
    if (p1_throw == 'Rock') and (p2_throw == 'Scissor'):
        p1_point += 1
        print("Player 1 Selected: ", player1_throw)
        print("Player 2 Selected: ", player2_throw)
        print("Player 1 Wins this game")
        
    elif (p1_throw == 'Scissor') and (p2_throw == 'Paper'):
        p1_point += 1
        print("Player 1 Selected: ", player1_throw)
        print("Player 2 Selected: ", player2_throw)
        print("Player 1 Wins this game")
        
    elif (p1_throw == 'Paper') and (p2_throw == 'Rock'):
        p1_point += 1
        print("Player 1 Selected: ", player1_throw)
        print("Player 2 Selected: ", player2_throw)
        print("Player 1 Wins this game")
        
    elif (p2_throw == 'Paper') and (p1_throw == 'Rock'):
        p2_point += 1
        print("Player 1 Selected: ", player1_throw)
        print("Player 2 Selected: ", player2_throw)
        print("Player 2 Wins this game")
        
    elif (p2_throw == 'Paper') and (p1_throw == 'Rock'):
        p2_point += 1
        print("Player 1 Selected: ", player1_throw)
        print("Player 2 Selected: ", player2_throw)
        print("Player 2 Wins this game")
        
    elif (p2_throw == 'Paper') and (p1_throw == 'Rock'):
        p2_point += 1
        print("Player 1 Selected: ", player1_throw)
        print("Player 2 Selected: ", player2_throw)
        print("Player 2 Wins this game")

    elif p1_throw == p2_throw:
        print("Player 1 Selected: ", player1_throw)
        print("Player 2 Selected: ", player2_throw)
        print("Game Tie No One Wins")
        
      

compare(player1_throw, player1_point,player2_throw, player2_point)

print("Player 1 Points: ", p1_point)
print("Player 2 Points: ", p2_point)






    


    

