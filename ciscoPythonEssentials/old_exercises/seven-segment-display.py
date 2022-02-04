#!/usr/bin/env python3


def digit_builder(digit_base):
    ### Parameters
    signals = {'a':('01', '02', '03'),
               'b':('14'),
               'c':('34'),
               'd':('41', '42', '43'),
               'e':('30'),
               'f':('10'),
               'g':('21', '22', '23')}

    numbers = {'1':('b', 'c'),
               '2':('a', 'b', 'e', 'd', 'g'),
               '3':('a', 'b', 'c', 'd', 'g'),
               '4':('b', 'c', 'f', 'g'),
               '5':('a', 'c', 'd', 'f' ,'g'),
               '6':('a', 'b', 'c', 'd', 'e', 'g'),
               '7':('a', 'b', 'c'),
               '8':('a', 'b', 'c', 'd', 'e', 'f', 'g'),
               '9':('a', 'b', 'c', 'd', 'f', 'g'),
               '0':('a', 'b', 'c', 'd', 'e', 'f')}

    digit = [[' ' for l in range(5)] for c in range(5)]

    simbol = numbers[digit_base]

    for signal in simbol:
        if signal in 'adg':
            for position in signals[signal]:
                digit[int(position[0])][int(position[1])] = '-'
        elif signal in 'bcef':
            digit[int(signals[signal[0]])][int(signals[signal[1]])] = '|'
    return digit
'''
    for line in range(len(digit)):
        for unit in range(len(digit[line])):
            if line % 2 == 0:
                if unit == 0 or unit == 4:
                    digit[line][unit] = ' '
                else:
                    digit[line][unit] = '-'
            else:
                if unit == 0 or unit == 4:
                    digit[line][unit] = '|'
'''

def display_builder(number):
    display = []
    number = str(number)
    for n in number:
        display.append(digit_builder(n))
    return display

def show_display(display):
    for line in range(len(display[0])):
        for digit in range(len(display)):
            print("".join(display[0][line]), end='  ')
        print()

def sample():
    line   = " ---"
    column = "|"
    center = " ---"

    ### Print 9
    print(line)
    print(column + ' '*3 + column)
    print(center)
    print(" "*4 + column)
    print(line)
    print()

    ### Print 8
    print()
    print(line   + '\n' + column + '   ' + column)
    print(center + '\n' + column + '   ' + column + '\n' + line)
    print()

    ### Print 7
    print(line)
    print(' '*4 + column)
    print()
    print(' '*4 + column)
    print()
    print()

    ### Print 6
    print(line)
    print(" "*4 + column)
    print(center)
    print(column + ' '*3 + column)
    print(line)
    print()

    ### Print 5
    print(line)
    print(column + " "*4)
    print(center)
    print(" "*4 + column)
    print(line)
    print()

    ### Print 4
    print()
    print(column + ' '*3 + column)
    print(center)
    print(" "*4 + column)
    print()
    print()

    ### Print 3
    print(line)
    print(' '*4 + column)
    print(center)
    print(' '*4 + column)
    print(line)
    print()

    ### Print 2
    print(line)
    print(" "*4 + column)
    print(center)
    print(column + " "*4)
    print(line)
    print()

    ### Print 1
    print()
    print(' '*4 + column)
    print()
    print(' '*4 + column)
    print()
    print()

    ### Print 0
    print(line)
    print(column + ' ' * 3 + column)
    print()
    print(column + ' ' * 3 + column)
    print(line)

### TEST AREA ###
if __name__ == '__main__':
    display = display_builder(888888)
    show_display(display)
