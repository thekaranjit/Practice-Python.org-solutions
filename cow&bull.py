import random
rand_range = 10
rand_length= 4

numbers = input("Input 4 digit number to guess : ")
random_num = random.sample(range(rand_range), rand_length)


numberlist = list(numbers)

numberlist = list(map(int, numberlist))

cow = 0
bull = 0

'''

for i in random_num:
    for j in numberlist:
        if i == j:
            cow += 1
        elif j != i:
            bull += 1 
'''

for i in random_num:
   if i in numberlist:
       cow += 1
   else:
       bull = 1
       

print("Generated Random Number is: ", random_num)
print("User Input is : ", numbers)
print("User input to list is: ", numberlist)
print(cow)
print(bull)

