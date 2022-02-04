from os import system
from random import randrange

global board
board= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def display_board(board):
    # The function accepts one parameter containing the board's current
    # status and prints it out to the console.
    height = 13
    width  = 25
    positions = []
    value = 0

    system("clear")
    print("TIC TAC TOE")

    for line in range(len(board)):
        for column in range(len(board[line])):
            positions.append(board[line][column])

    for y in range(height):
        if y % 4 == 0:
            for x in range(width):
                if x % 8 == 0:
                    print("+", end="")
                else:
                    print("-", end="")
            print()
        else:
            for x in range(width):
                if y in (2, 6, 10) and (x % 4 == 0 and x % 8 != 0):
                    print(positions[value], end="")
                    value += 1
                    continue
                if x % 8 == 0:
                    print("|", end="")
                else:
                    print(" ", end="")
            print()
    return

def enter_move(board):
    # The function accepts the board current status, asks the user about
    # their move, checks the input and updates the board according to
    # the user's decision.
    display_board(board)
    move = input("Choose a free position to play: ")

    if not move.isnumeric():
        return invalid_move()

    for line in range(len(board)):
        for column in range(len(board[line])):
            if int(move) == board[line][column]:
                board[line][column] = "O"
                return
    return invalid_move()

def invalid_move():
    #display_board(board)
    print("Invalid move, try again in an available position.")
    input()
    enter_move(board)

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free
    # squares; the list consists of tuples, while each tuple is a pair
    # of row and column numbers.
    free_fields = []
    for line in range(len(board)):
        for column in range(len(board[line])):
            if type(board[line][column]) is int:
                free_fields.append((line,column))
    return free_fields

def victory_for(board, sign):
    # The function analyzes the board status in order to check if
    # the player using 'O's or 'X's has won the game
    if   sign == board[0][0]:
        if ((board[0][1] == sign == board[0][2]) or
            (board[1][0] == sign == board[2][0]) or
            (board[1][1] == sign == board[2][2])): return True
    if sign == board[0][1]:
        if (board[1][1] == sign == board[2][1]): return True
    if sign == board[0][2]:
        if  ((board[1][1] == sign == board[1][2]) or
             (board[1][2] == sign == board[2][2])): return True
    if sign == board[1][0]:
        if (board[1][1] == sign == board[1][2]): return True
    if sign == board[2][0]:
        if (board[2][1] == sign == board[2][2]): return True
    return False

def draw_move(board):
    # The function draws the computer's move and updates the board.
    free_fields = make_list_of_free_fields(board)
    move = free_fields[randrange(1, len(free_fields))]
    display_board(board)
    print(f"The machine marked position {board[move[0]][move[1]]}")
    input()
    board[move[0]][move[1]] = "X"
    return

def start_game():
    reset_board()
    display_board(board)
    print("\n\n Welcome to the  game.\nPress any key to start.")
    input()
    ongoing(board)
    return

def reset_board():
    position = 1
    global board
    for line in range(len(board)):
        for column in range(len(board[line])):
            board[line][column] = position
            position += 1
    return

def ongoing(board):
    turn = 1
    while len(make_list_of_free_fields(board)) > 1:
        if turn % 2 == 0:
            enter_move(board)
            if victory_for(board, "O"):
                end_game("Congratulations you won!")
                return
        else:
            draw_move(board)
            if victory_for(board, "X"):
                end_game("The machine won, more luck next time!")
                return
        turn += 1
    end_game("No winners.")
    return

def end_game(message):
    display_board(board)
    print(message)
    answer = input("Do you want to play again? [y/n]")
    if answer[0].capitalize() == "Y":
        start_game()
    return

if __name__  == "__main__":
    start_game()

