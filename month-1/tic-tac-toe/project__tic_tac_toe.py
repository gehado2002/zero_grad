def create_empty_board():
    board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

    for i in board:
        for j in i:
            print(j, end="\t")
        print('\n')
    return board

#create_empty_board()

"""## Show Board"""

def show_board(board):
    for i in board:
        for j in i:
            print(j, end="\t")
        print('\n')

#board = [[1,2,3],[4,'X',6],[7,8,9]]
#show_board(board)

"""## Set Players"""

import random
def set_players():
    player=random.choice(('X', 'O'))
    if player == 'X':
        return ('X', 'O')
    else :
        return ('O', 'X')

#set_players()

"""## Take Input"""

def take_input(board, player):
        num=int(input("Please Enter a number between 1,9 represents an empty position:    "))

        if num>=1 and num<=9:
            row = (num - 1) // 3
            col = (num - 1) % 3

            if board[row][col].isdigit():
                board[row][col] = player
            else:
                print("invalid choice")

        show_board(board)

board = [['1','2','3'],['4','X','6'],['7','8','9']]
player ='O'
player_input = '8'
#take_input(board, player)

"""## Check Full Board"""

# how to Check Full Board
def check_full_board(board):
    for i in board:
        for j in i:
            if j.lower() =='o' or j.lower()=='x':
                continue
            else :
                return False


    return True

board = [['o','x','x'],['o','X','o'],['x','o','x']]
#check_full_board(board)

board = [['o','x','x'],['4','X','o'],['x','o','x']]
#check_full_board(board)

"""## Check Win

"""

def check_win(board):
    for row in board:
        if row[0] == row[1] == row[2] :
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] :
            return True
    # two diagonals
    if board[0][0] == board[1][1] == board[2][2] :
        return True
    if board[0][2] == board[1][1] == board[2][0] :
        return True
    return False

board = [['o','x','x'],['o','o','x'],['x','o','x']]
#show_board(board)
check_win(board)

board = [['o','x','o'],['o','o','x'],['x','o','x']]
#show_board(board)
#check_win(board)

"""## Let's Play"""

def play():
    player1, player2 = set_players()
    board = create_empty_board()

    while True:
        print(f"Player {player1} turn ")
        take_input(board, player1)

        if check_win(board):
            print(f"Player {player1} wins!")
            break
        if check_full_board(board):
            print("It's a draw!")
            break

        print(f"Player {player2} turn ")
        take_input(board, player2)

        if check_win(board):
            print(f"Player {player2} wins!")
            break
        if check_full_board(board):
            print("It's a draw!")
            break

play()
