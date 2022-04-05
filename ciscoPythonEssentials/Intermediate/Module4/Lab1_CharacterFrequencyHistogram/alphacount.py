#!/usr/bin/python
from os import strerror

file = input('Enter the name of the file containing the text to parse: ')
#file = 'test2'
recurrence = {}

try:
    stream = open(file, 'rt')
    for line in stream:
        for letter in line:
            if letter.isalpha():
                if letter.lower() in recurrence:
                    recurrence[letter.lower()] += 1
                else:
                    recurrence[letter.lower()] = 1
    stream.close()
except IOError as e:
    print('I/O error occurred:', strerror(e.errno))

for key, value in sorted(recurrence.items()):
    print(key + '| ' + '===' * value) 

highest = recurrence[max(recurrence, key=recurrence.get)]
print('  ' + '-'*(highest*3))
print(' '* 4, end='')

for pos in range(highest):
    if len(str(pos)) < 2:
        mark = '0' + str(pos+1)
    else:
        mark = str(pos+1)
    print(mark, end=' ')

