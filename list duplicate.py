
import random

# get range & length of list
list_range = int(input("Please input the range of list to be generated: "))
list_length = int(input("Please input the length of list to be generated: "))

# generate random list
rand_list = random.sample(range(list_range), list_length)
# create an empty list
final_list = []

#remove duplicates
cleanlist = list(set(rand_list))

        
    
# print duplicate
print(rand_list)
print("Final Without Duplicate list is: ", cleanlist)
