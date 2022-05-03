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
    return dict(sorted(dic.items()))

def sort_by_recurrence(dic):
    ''' dict >> dict
    Receive a dictionary and reorganize it
    in the descending order of occurence (values).
    '''
    return dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))

def build_histogram(dic, sorted_by='alpha'):
    ''' dict >> print
    Receive a dictonary and print a histogram
    '''
    # Set dictionary sorting
    if sorted_by == 'alpha':
        dic = sort_alphabetically(dic)
    elif sorted_by == 'occ':
        dic = sort_by_recurrence(dic)
    else:
        print('Error:\nInvalid parameter.')
        return
    
    # Store the histogram in a list
    histogram = []
    for key, value in dic.items():
        histogram.append((key + '|' + '===' * value))
    
    highest = dic[max(dic, key=dic.get)]
    histogram.append('  ' + '--' + '-' * (highest*3))
    
    last_line = ' 00 '

    for position in range(highest):
        if position < 9:
            mark = '0' + str(position + 1)
        else:
            mark = str(position + 1)
        last_line += mark + ' '
    histogram.append(last_line)
    return histogram

def write_output(histogram, filename):
    filename = filename.split('.')[0]
    output_file = open(filename + '.hist', 'wt')


    output_file.close()
    pass


if __name__ == '__main__':
    #file = input('Enter the name of the file containing the text to parse: ')
    file = 'test2'
    '''
    print('Result by alphabeticall order:')
    print(sort_alphabetically(recurrence(file)))
    print('Result by order of occurrence:')
    print(sort_by_recurrence(recurrence(file)))
    print('Analyzing the text below:')
    for line in open(file, 'rt'):
        print(line)
    '''

    print('Histogram:\n')

    hist = build_histogram(recurrence(file), 'occ')
    for line in hist:
        print(line)

