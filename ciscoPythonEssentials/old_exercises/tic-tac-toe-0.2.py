from os import system
from random import randrange


def sample():
    sample_board = """
    +-------+-------+-------+
    |       |       |       |
    |   1   |   2   |   3   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   4   |   5   |   6   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   7   |   8   |   9   |
    |       |       |       |
    +-------+-------+-------+"""
    print("This is an example of a board:\n", sample_board)
    return

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

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
    if len(make_list_of_free_fields(board)) > 0:
        move = input("Choose a free position to play: ")
        if move.isnumeric():
            found = False
            for line in range(len(board)):
                for column in range(len(board[line])):
                    if int(move) != board[line][column]:
                        print(f"Caso{move} ==> {board[line][column]}")
                        input()
                        continue
                    else:
                        board[line][column] = "O"
                        found = True
                        break
                    if not found: invalid_move()
            draw_move(board)
        else:
            invalid_move()
    else:
        victory_for(board, "O")
    display_board(board)

    return

def invalid_move():
    display_board(board)
    print("Invalid move, try again in an available position.")
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
    return

def draw_move(board):
    # The function draws the computer's move and updates the board.
    free_fields = make_list_of_free_fields(board)
    if len(free_fields) < 0:
        move = free_fields[randrange(1, len(free_fields))]
        board[move[0], move[1]] = "X"
        enter_move()
    else:
        victory_for(board, "X")

    return

def play_game():
    display_board(board)
    enter_move(board)

if __name__ == "__main__":
    play_game()
