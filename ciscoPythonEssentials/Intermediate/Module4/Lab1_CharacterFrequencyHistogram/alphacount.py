#!/usr/bin/python
from os import strerror

def recurrence(filename, sort_by='occ'):
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

    # Sort data by 
    if sort_by == 'alpha':
        recurrence = dict(sorted(recurrence.items()))
    else:
        recurrence = dict(sorted(recurrence.items(), key=lambda item: item[1], reverse=True))

    # Write output in a file
    write_output(histogram(recurrence), filename)
    pass

def histogram(data):
    ''' dict >> list
    Receive a dictonary histogram
    '''
    # Store the histogram in a list
    histogram = []
    for key, value in data.items():
        histogram.append((key + '|' + '===' * value))
    
    highest = data[max(data, key=data.get)]
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
    for line in histogram:
        output_file.write(line + '\n')
    output_file.close()
    pass

if __name__ == '__main__':
    file = input('Enter the name of the file to be evaluated: ')
    recurrence(file)
