#!/usr/bin/env python3
def mysplit(string):
    new_list = []
    if string.isspace() or len(string) == 0:
        return new_list

    string = string.strip()
    if not ' ' in string:
        new_list.append(string)
        return new_list

    word = ''
    for ch in string:
        if ch != ' ':
            word += ch
        else:
            new_list.append(word)
            word = ''
    # Add the last word
    new_list.append(word)

    return new_list

if __name__ == '__main__':
    # Expected results
    result1 = ['To', 'be', 'or', 'not', 'to', 'be,', 'that', 'is', 'the', 'question']
    result2 = ['To', 'be', 'or', 'not', 'to', 'be,that', 'is', 'the', 'question']
    result3 = []
    result4 = ['abc']
    # Data to input
    test1 = mysplit('To be or not to be, that is the question')
    test2 = mysplit('To be or not to be,that is the question')
    test3 = mysplit('  ')
    test4 = mysplit('   abc    ')
    test5 = mysplit('')
    # List with the input and expected results
    template = [[test1, result1], [test2, result2], [test3, result3], [test4, result4], [test5, result3]]
    # Running tests
    for test in range(len(template)):
        print('#'*30)
        print(f"Test {test+1} ", end="")
        if template[test][0] == template[test][1]:
            print("Pass.")
        else:
            print("Error.")
            print(f"""Expected:{template[test][1]} \nReceived:{template[test][0]}""")
            print()
