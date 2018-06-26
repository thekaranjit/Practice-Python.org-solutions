
def data():
    return int(input("Please input a data: "))

input_num = data()


if input_num > 1:
    for i in range(2, input_num):
        if (input_num % i) == 0:
            print(input_num, ": Is a not prime number.")
            print (i, "times", input_num//i, "is", input_num )
            break
            
    else:
        print(input_num, ": is a prime number.")
        
else:
    print(input_num, ": is not a prime number.")
               
               
