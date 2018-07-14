'''
def draw():
    board = ''

    for i in range(-1,6):

        if i%2==0:
            board += '|      ' * 4
            board += '\n|      |      |      |'

        else:
            board += ' _____ ' * 3

        board += '\n'
    print (board)

draw()

'''


gameboard_size = int(input("PLease input the size of board you required \n 1. For 3x3 Size  \n 2. For 8x8 size: \n 3. For 19x19 Size\n Enter your Selection: "))

def gameboard1():
    for i in range(3):
        board = ' ---' *3
        board2= '|   '*4
        board3 = ' ---' *3
        print(board)
        print(board2)
    print(board3)
        

def gameboard2():
    for i in range(8):
        board = ' ---' *8
        board2= '|   '*9
        board3 = ' ---' *8
        print(board)
        print(board2)
    print(board3)

def gameboard3():
    for i in range(18):
        board = ' ---' *18
        board2= '|   '*19
        board3 = ' ---' *18
        print(board)
        print(board2)
    print(board3)
    
    

if gameboard_size == 1:
    print("Game Board of 3 x 3 Size :- ")
    gameboard1()
    
elif gameboard_size == 2:
    print("Game Board of 8 x 8 Size :- ")
    gameboard2()

elif gameboard_size == 3:
    print("Game Board of 19 x 19 Size :- ")
    gameboard3()

else:
    print("Please input correct selection")
