
import random

# Generate Random Numbers List1 & List2
num_range = int(input("Please Input Max range of list: "))
num_length = int(input("Please input the length of list you wish to generate: "))



rand_list1=random.sample(range(num_range), num_length)
rand_list2=random.sample(range(num_range), num_length)


# finding common number from generated random list and save in new_list
new_list = []

for i in rand_list1:
    for j in rand_list2:
        if i == j:
            new_list.append(i)
            

# delete all the duplicate entries from new_list
cleanlist = list(set(new_list))

# find & calsulate length of all generated lists
lengthlist1 = len(rand_list1)
lengthlist2 = len(rand_list2)
lengthlist3 = len(new_list)
lengthlist4 = len(cleanlist)

# output all the random lists s
print("Random List1: ", rand_list1)
print("Random List2: ", rand_list2)
print("Random with common numbers: ", new_list)
print("Random List without copy: ", cleanlist)

print()

print("Length of Random List1: ", lengthlist1)
print("Length of Random List2: ", lengthlist2)
print("Length of Random with common numbers: ", lengthlist3)
print("Length of Random List without copy: ", lengthlist4)

        
