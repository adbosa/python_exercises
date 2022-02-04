#!/usr/bin/python
##########################################
## CAESAR CIPHER - CISCO PYTHON ESSENTIALS
##########################################

def main():
    phrase = ''
    while len(phrase.strip()) < 1:
        phrase = input('Enter the phrase to be encrypted: ')

    shift = 0
    while type(shift) != int or shift < 1 or shift > 25:
        try:
            shift = int(input('Insert the cipher to be used[1-25]: '))
        except:
            print('You must insert a number between 1 and 25. Try again')
    print(encript(phrase, shift))



def encript(phrase, shift):
    new_phrase = ''

    for ch in phrase:
        if not ch.isalpha():
            new_phrase += ch
        else:
            new_phrase += cipher(ch,shift)
    return new_phrase
def cipher(letter, shift):
    if ord(letter) <= 90:
        letter = ord(letter) + shift
        if letter > 90:
            letter = (letter - 90) + 64
    else:
        letter = ord(letter) + shift
        if letter > 122:
            letter = (letter - 122) + 96
    return chr(letter)

### runtime
if __name__ == "__main__":
    # Example data
    example_input  = {'abcxyzABCxyz 123':2, 'The die is cast':25}
    example_output = ['cdezabCDEzab 123', 'Sgd chd hr bzrs']

    for i in range(len(example_input)):
        phrase    = list(example_input.keys())[i]
        shift_key = list(example_input.values())[i]
        output    = example_output[i]

        if encript(phrase,shift_key) == output:
            print(f'Test {i+1} - Success')
        else:
            print(f'Test {i+1} - Fail')
            print(f'Send:     {phrase}')
            print(f'Key:      {shift_key}')
            print(f'Expected: {example_output[i]}')
            print(f'Obtained: {encript(phrase, shift_key)}\n')
