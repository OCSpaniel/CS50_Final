import sys
import os
import time
import random
import helper as help

while True:
    board = [""," "," "," "," "," "," "," "," "," "]
    help.printHeader()
    help.printBoard(board)
    player_letter, computer_letter = help.chooseLetter()
    turn = help.whoGoesFirst()
    print ("The {} will go first.".format(turn))
    gameActive = True #Set variable for loop
    
    while gameActive:
        if turn == 'player':
            help.printBoard(board) #Begin player's turn
            choice = help.getMove(board)
            board[choice] = player_letter
            help.printBoard(board)

            if help.is_winner(board, player_letter):
                help.printBoard(board)
                print("Congratulations you have won")
                gameActive = False
            else:
                if help.boardFull(board):
                    help.printBoard(board)
                    print('The game is a tie')
                    break
                else:
                    turn = 'computer' # Set turn equal to computer
            
        else: #Begin Computer's turn loop
            print("Beginning Computer's Turn")
            comp_move = help.computerMove(board, computer_letter)
            board[comp_move] = computer_letter  
            if help.is_winner(board, computer_letter):
                help.printBoard(board)
                print("The computer has won :(")
                gameActive = False
            else:
                if help.boardFull(board):
                    help.printBoard(board)
                    print('The game is a tie')
                    break
                else:
                    turn = 'player'

    if not help.wantToPlay():
        break




    
    
