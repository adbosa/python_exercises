#!/home/alex/.asdf/shims/python

def theDigitOfLife(birthday):
    digitOfLife = birthday
    while len(str(digitOfLife)) > 1:
        aux_sum = 0
        for number in str(digitOfLife):
            aux_sum += int(number)
        digitOfLife = aux_sum
    return digitOfLife

if __name__ == "__main__":
    tests= [[19991229, 6], [20000101, 4]]
    test_number = 0
    for test in tests:
        test_number += 1
        print(f"{test_number} test: ", end="")
        if theDigitOfLife(test[0]) == test[1]:
            print("Pass")
        else:
            print("Fail")
