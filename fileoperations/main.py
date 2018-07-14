
import re
from collections import Counter


'''
 Below is my tries
 
# write mode , to write and overwrite all the content
f = open("karan.txt", "w")
f.write("I Love Python")
f.close()

# write mode , to write and append the content (Keep old data and add new one)
f = open("karan.txt", "a")
f.write("\nI Love Java Script")
f.close()

f = open("karan.txt", "r")
f_out = open("karan2.txt", "w")

for line in f:
    tokens = line.split(' ')
    token_len = len(tokens)
    f_out.write("\nWordcount: " +  str(token_len) + line )
    print(line)
    print(tokens)
    print(token_len)



#print(f.read()) --------------> to read and print all the content in file

f.close
f_out.close

f = open("nameslist.txt", "r")
all_text = open_file.read()


with open('nameslist.txt', 'r') as open_file:
    all_text = open_file.read()

name_list = []
res = name_list.append(all_text, 0)


with open('nameslist.txt', 'r') as open_file:
    all_text = open_file.read()

#print(all_text)
word_list = []
word_list = all_text.split()
for item in word_list:
    word_list.append(item)


print(word_list)

for line in f:
    tokens = line.split(' ')
    token_len = len(tokens)
    #print(line)
    #print(tokens)
    #print(token_len)
    for list in tokens:
        a.extend(list)
        print(a)

'''




with open ("nameslist.txt", "r") as myfile:
    data=myfile.readlines()

clean = []

for item in data:
    clean.append(re.sub('\n', '', item))

result_file = Counter(clean)

print("Our Extracted data from text file is: ", data)
print("Our Cleaned file is: ", clean)
print("Our final result file is: ", result_file)


