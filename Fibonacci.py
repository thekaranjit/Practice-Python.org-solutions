user_range = int(input("Please input the range of numbers to generate a Fibonacci  series : "))


list=[x for x in range(0,user_range)]

new_list = []
a = 0

for i in range(user_range):
    for j in list:
        a = j
        new_list.append(j)
        
     
     
print(list)
print(i)

print(new_list)



