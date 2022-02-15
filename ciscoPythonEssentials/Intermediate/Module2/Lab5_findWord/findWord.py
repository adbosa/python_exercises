#!/usr/bin/python

'''
Let's play a game. We will give you two strings: one being a word (e.g., "dog")
and the second being a combination of any characters.

Your task is to write a program which answers the following question: are the
characters comprising the first string hidden inside the second string?

Hints

Using the find() method for searching strings.
You should use the two-argument variants of the pos() functions inside your code;
'''


def is_word_inside(word, sentence):
    for letter in word:
        if sentence.find(letter) == -1:
            return False
    return True 

if __name__ == "__main__":
    tests = [["donor", "Nabucodonosor", True], ["donut", "Nabucodonosor", False]]
    test_number = 0

    for test in tests:
        test_number += 1
        print(f"Test {test_number} :", end=" ")
        if is_word_inside(test[0], test[1]) == test[2]:
            print("Pass.")
        else:
            print("Fail.")
