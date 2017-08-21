import random

board = [""," "," "," "," "," "," "," "," "," "]

def printHeader():
    print("""
     _   _      _             _      
    | | (_)    | |           | |                1 | 2 | 3
    | |_ _  ___| |_ ___   ___| |_ ___   ___     4 | 5 | 6
    | __| |/ __| __/ _ | /___| |_/ _ \ / _ \    7 | 8 | 9
    | |_| | (__| || (_| | (__| || (_) |  __/
    \__ |_|\___|\__\__,_|\___|\__\___/ \___|
    """)
    print('\n')
    print('\n')

def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def chooseLetter():
    #Player Chooses X or O

    letter = ''
    while not (letter =='X' or letter == 'O'): #keep asking until they enter an X or an O
        print("Choose X or O.")
        letter = input().upper() #ensure whether they input upper or lowercase, upper is chosen

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O','X']

def whoGoesFirst(): #random function to determine who goes first. Returns string to print
    if random.randint(0,1) == 0:
        return "computer"
    else:
        return "player"

def checkFreeSpace(board, choice):
    if board[choice] == " ":
        return board[choice] 

def is_winner(board, player): #Win checking routine (8 possibilities)
    if (board[1] == board[2] == board[3] == player) or \
        (board[4] == board[5] == board[6] == player) or \
        (board[7] == board[8] == board[9] == player) or \
        (board[1] == board[4] == board[7] == player) or \
        (board[2] == board[5] == board[8] == player) or \
        (board[3] == board[6] == board[9] == player) or \
        (board[1] == board[5] == board[9] == player) or \
        (board[3] == board[5] == board[7] == player):
        return True
    else:
        return False

def computerMove(board, letter):
    if board[5] != 'X' and board[5] !='O':
        return 5
    while True:
        random.seed()
        comp_rand_move = random.randint(1,9)
        if board[comp_rand_move] == " ":
            return comp_rand_move
            break

def wantToPlay(): 
    print('Do you want to play again? (y or n)')
    return input().lower().startswith('y') #should capture y or Yes or Y otherwise return a False


def boardFull(board): #Function to check if board is full (tie)
    for i in range (1,10):
        if checkFreeSpace(board, i):
            return False
    return True

def getMove(board):
    move = ''
    while move not in '1 2 3 4 5 6 7 8 9'.split()  or not checkFreeSpace(board, int(move)):
        print('Please select 1-9 that is unoccupied')
        move = input()
    return int(move)

def randomMove(board): #Generate random move, check if occupised, place marker if unoccupied
    seeking = True
    while seeking:
        random.seed()
        comp_move = random.randint(0,8)
        if board[comp_move] != 'O' and board[comp_move] != 'X':
            return int(comp_move)
        else:
            seeking = False
        break
