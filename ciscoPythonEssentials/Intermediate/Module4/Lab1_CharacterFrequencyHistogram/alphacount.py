#!/usr/bin/python
from os import strerror

def recurrence(filename):
    ''' text file >> dict
    Take a text file and in order of occurrence and
    create a dictionary counting how many times each
    character appears.
    '''
    recurrence = {}
    try:
        stream = open(filename, 'rt')
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
    return recurrence

def sort_alphabetically(dic):
    ''' dict >> dict
    Receive a dictionary and reorganize it
    in the alphabetical order (keys).
    '''
    return sorted(dic.items())

def sort_by_recurrence(dic):
    ''' dict >> dict
    Receive a dictionary and reorganize it
    in the descending order of occurence (values).
    '''
    return dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))

def build_histogram(dic, sorted_by='alpha'):
    pass

def write_output(histogram, filename):
    pass


"""
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
"""
if __name__ == '__main__':
    #file = input('Enter the name of the file containing the text to parse: ')
    file = 'test2'
    print('Result by alphabeticall order:')
    print(sort_alphabetically(recurrence(file)))
    print('Result by order of occurrence:')
    print(sort_by_recurrence(recurrence(file)))
