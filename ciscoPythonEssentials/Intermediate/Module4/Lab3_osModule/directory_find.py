#!/usr/bin/python

def find(path, target):
    import os

    for directory in os.listdir(path):
        sub_path = path + '/' + directory
        if target.lower() in directory.lower():
            print(os.path.abspath(sub_path))
            return
        if not os.path.isdir(sub_path):
            return
        for sub_directory in os.listdir(sub_path):
            if not os.path.isdir(sub_path):
                return
            if len(os.listdir(sub_path)) < 1:
                return
            else:
                find(sub_path + '/' + sub_directory, target)


if __name__ == '__main__':
    find(path='./tree', target='python')
