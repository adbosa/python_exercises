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
    return None

def validate_group(number_list):
    number_list = str(number_list)
    for number in number_list:
        if number_list.count(number) > 2:
            return True
    return False



if __name__ == "__main__":
    tests = [[[295743861, 431865927, 876192543,
            387459216, 612387495, 549216738,
            763524189, 928671354, 154938672], True],
            [[195743862, 431865927, 876192543,
            387459216, 612387495, 549216738,
            763524189, 928671354, 254938671], False]]
    test_number = 0

    print("Test validate group.\n")
    if validate_group(tests[0][0][0])

    print("\n"*2)
    print("Test board validation.\n")
    for test in tests:
        test_number += 1
        print(f"Test number {test_number}:", end=" ")
        if game_validation(test[0]) == test[1]:
            print("Pass")
        else:
            print("Fail")


