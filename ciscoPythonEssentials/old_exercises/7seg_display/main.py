#!/usr/bin/env python3

def main():
    user_num = received_number()
    return

def received_number():
    user_num = ''
    while type(user_num) != int:
        user_num = int(input('Insert a integral non negative number: '))
    return user_num

### TEST AREA ###
if __name__ == '__main__':
    print('Let\'s go.')

