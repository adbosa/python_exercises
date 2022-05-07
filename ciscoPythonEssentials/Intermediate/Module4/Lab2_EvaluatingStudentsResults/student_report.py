#!/usr/bin/python
'''
Write a program which:
* asks the user for file name;
* reads the file contents and counts the sum of the received points for each student;
* prints a simple (but sorted) report, just like this one:
    
    Andrew Cox 	 1.5
    Anna Boleyn 	 15.5
    John Smith 	 7.0
'''
from os import strerror

class StudentsDataException(Exception):
    pass

class BadLine(StudentsDataException):
    def __init__(self, line_number, line_string):
        StudentsDataException.__init__(self)
        self.line_number = line_number
        self.line_string = line_string

class FileEmpty(StudentsDataException):
    def __init__(self):
        super().__init__(self)

def main():
    filename = input('Enter the name of the file with student grades: ')
    raw_students_grade = extract_data(filename)
    final_students_grade = clean_notes(raw_students_grade)
    return final_students_grade

def extract_data(filename):
    raw_notes = []
    try:
        stream = open(filename, 'rt')
        lines_notes = stream.read().splitlines()
        for line in lines_notes:
            raw_notes.append(line.split('\t'))
        stream.close()
        if len(raw_notes) < 1:
            raise FileEmpty

    except IOError as e:
        print('I/O error occurred: ' + strerror(e.errno))
    except EmptyFile:
        print('Source file empty.')
    
    return raw_notes

def clean_notes(raw_notes):
    clean_notes = {}
    for line in range(len(raw_notes)):
        name = ''
        grade = ''
        name_length = len(raw_notes[line]) - 1
        for item in range(name_length + 1):
            if item < name_length:
                name += raw_notes[line][item] + ' '
            else:
                try:
                    grade = float(raw_notes[line][item])
                except ValueError:
                    raise BadLine(line + 1, raw_notes[line][item])
                except BadLine as e:
                    print('Bad line #' + str(e.line_number) + ' in source file:' + line_string)
        name = name.rstrip()
        if name in clean_notes:
            clean_notes[name] += grade
        else:
            clean_notes[name] = grade
    return clean_notes

def print_grade(grade):
    for key, value in sorted(grade.items()):
        print(f'{key}\t {value}')

if __name__ == '__main__':
    # print(extract_data('my_notes'))
    # print(clean_notes(extract_data('my_notes')))
    print_grade(clean_notes(extract_data('my_notes')))

