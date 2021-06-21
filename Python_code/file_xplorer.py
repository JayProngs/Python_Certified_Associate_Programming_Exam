import os


def find(dirct, path="tree"):
    os.chdir(path)
    for dirs in os.listdir():
        if dirs == dirct:
            print(os.getcwd() + "\\" + dirct)
        find(dirct, dirs)
    os.chdir('../')


find('python')