#!/usr/bin/python
'''
reads 9 rows of the Sudoku, each containing 9 digits
(check carefully if the data entered are valid),
outputs "Yes" if the Sudoku is valid, and "No" otherwise.

Objectives

* improving the student's skills in operating with strings and lists;
* converting strings into lists.
'''

def game_validation(board):
    ### Valid line
    for line in board:
        if not validate_group(line): return False
    ### Valid columns
    for i in range(9):
        column = []
        for line in board:
            column.append(str(line)[i])
        if not validate_group(''.join(column)): return False
    ### Valid sub-square
    for i in range(9):
        print()
        for j in range(3):
            print(str(board[i])[j], end="")
        if (i + 1) % 3 == 0: print()
    print()



    return None

def validate_group(number_list):
    number_list = str(number_list)
    for number in number_list:
        if number_list.count(number) > 1:
            return False 
    return True



if __name__ == "__main__":
    
    group_test = [[123456789, True],
                  [123455789, False],
                  [984673214, False]]
    test_number = 0
    print("Test validate group.\n")
    for test in group_test:
        test_number += 1
        print(f"Test number {test_number}:", end=" ")
        if validate_group(test[0]) == test[1]:
            print("Pass")
        else:
            print("Fail")
    

    tests = [[[295743861, 431865927, 876192543,
            387459216, 612387495, 549216738,
            763524189, 928671354, 154938672], True],
            [[195743862, 431865927, 876192543,
            387459216, 612387495, 549216738,
            763524189, 928671354, 254938671], False]]
    test_number = 0
    print("\n"*2)
    print("Test board validation.\n")
    for test in tests:
        test_number += 1
        print(f"Test number {test_number}:", end=" ")
        if game_validation(test[0]) == test[1]:
            print("Pass")
        else:
            print("Fail")


