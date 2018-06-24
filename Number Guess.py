import sys
from random import randrange

number_guess = int(input("Please guess a number between 1 to 9 :"))

num1 = randrange(0, 10)

'''

if (number_guess - num1) == 1:
    print("You are almost lose by 1")
    
        
elif (number_guess - num1) == 2:
    print("You are almost lose by 2")
           
            
elif (number_guess - num1) == 3:
    print("You are almost lose by 4")
    
        
elif (number_guess - num1) >= 4:
    print("You are Very Far from the guess number")
    
else:
    print("You lost this game please try again")
    
'''
    
def guess_number(num_guess, nu1):
    if (num_guess - nu1) == 1:
        print("You are almost lose by 1")
        
            
    elif (num_guess - nu1) == 2:
        print("You are almost lose by 2")
               
                
    elif (num_guess - nu1) == 3:
        print("You are almost lose by 4")
        
            
    elif (num_guess - nu1) >= 4:
        print("You are Very Far from the guess number")
        
         
    else:
        print("You lost this game please try again")
        
        


guess_number(number_guess, num1)

print("The actual number is: ", num1)
print("But You Entered: ", number_guess)

