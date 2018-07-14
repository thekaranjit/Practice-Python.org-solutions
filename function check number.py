import random

num_range = 20
num_length = 10

random_list=random.sample(range(num_range), num_length)

num_sorted = sorted(random_list)

print(num_sorted)

num_guess = int(input("Please input a number to check: "))

'''

if num_guess in num_sorted:
    print("This Number is present in list")
    
else:
    print("Number is not present in list")

'''

def findnum(a, b):
    if b in a:
        print("This Number is present in list")
    else:
        print("Number is not present in list")
    
    
       
      
    
findnum(num_sorted, num_guess)


