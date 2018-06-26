# import random module
import random

# get input range from user (Range of list & length of list)
list_range = int(input("Please input range of list: "))
list_length = int(input("Please input length of list: "))

# generate random list
rand_list = random.sample(range(list_range), list_length)

# extract 1st and last element of list
list_1 = rand_list[0]
list_2 = rand_list[-1]

# make new list with first & last element of the list 
final_list = []

final_list.append(list_1)
final_list.append(list_2)
    

# print the result

print("Generated Random List is: ", rand_list)
print("First element of list is : ", list_1)
print("Last element of the list is : ", list_2)
print("Result list with first & Last element from generated random list is : ", final_list)