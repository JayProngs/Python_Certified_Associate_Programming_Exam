"""
Write a function or method called find that takes two arguments called path and dir. The path argument should accept a relative or absolute path to a directory where the search should start, while the dir argument should be the name of a directory that you want to find in the given path. Your program should display the absolute paths if it finds a directory with the given name.
The directory search should be done recursively. This means that the search should also include all subdirectories in the given path.
"""

import os


def find(dirct, path="tree"):
    os.chdir(path)
    for dirs in os.listdir():
        if dirs == dirct:
            print(os.getcwd() + "\\" + dirct)
        find(dirct, dirs)
    os.chdir('../')


find('python')
