import re
from collections import Counter

'''
with open("training.txt", "r") as myfile:
    data = myfile.readlines()



print (data)

'''

text_file = open("training.txt", "r")

#lines = text_file.read().split('/')

clean = []


for item in text_file:
    clean.append(re.sub('\n', '', item))

listoflist = [l.split(',') for l in ','.join(clean).split('/')]

a = list(filter(lambda x: x!= '', listoflist))






#print(clean)
#print(listoflist)





'''
clean = []

for item in lines:
    clean.append(re.sub('\n', '', item))

print(clean)




clean = []

for item in data:
    clean.append(re.sub('\n', '', item))

result_file = Counter(clean)

print("Our Extracted data from text file is: ", data)
print("Our Cleaned file is: ", clean)
print("Our final result file is: ", result_file)

'''
