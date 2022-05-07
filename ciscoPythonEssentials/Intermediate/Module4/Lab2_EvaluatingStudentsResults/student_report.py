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
def main():
    filename = input('Enter the name of the file with student grades: ')
    return clean_notes(filename).sort()

def clean_notes(filename):
    stream = open(filename, 'rt')
    notes = {}
    for line in stream:
        name = ''
        grade = ''
        name_length = len(line.split()) - 1
        for item in range(name_length + 1):
            if item < name_length:
                name += line.split()[item] + ' '
            else:
                grade = float(line.split()[item])
        name = name.rstrip()
        if name in notes:
            notes[name] += grade
        else:
            notes[name] = grade
    stream.close()
    return notes

def print_grade(grade):
    for key, value in sorted(grade.items()):
        print(f'{key}\t {value}')

if __name__ == '__main__':
    print_grade(clean_notes('my_notes'))
