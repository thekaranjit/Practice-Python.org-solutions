'''
Generate a random list.
Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
'''
import random
num_range = int(input("Please Input Max range of list: "))
num_length = int(input("Please input the length of list you wish to generate: "))


rand_list=random.sample(range(num_range), num_length)

even_list = []
'''
below code for single line
even_list = (elist for elist in rand_list if i% 2 == 0) 

'''

for i in rand_list:
    if i%2 == 0:
        even_list.append(i)


        
for j in even_list:
    if i%2 != 0:
        print("There is no even number in generated list")

print("The Generated Random list is: ", rand_list)
print("The Generated Even numbers from the list is: ", even_list)


