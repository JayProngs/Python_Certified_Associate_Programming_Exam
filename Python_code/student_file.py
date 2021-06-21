"""
File which is read need to have next new line as last record else code will fail
"""
from os import strerror


def sort_dict(d):
    return dict(sorted(d.items(), key=lambda item: item[1]))


name = marks = ''
diction = {}
filein = 'stud'  # input('Enter filename :')
try:
    buffer = open(filein + '.txt', 'r')
    ch = buffer.read(1)
    while ch != '':
        while ch != '\t':
            name = name + ch
            ch = buffer.read(1)
        name = name + '\t'
        ch = buffer.read(1)
        while ch != '\t':
            name = name + ch
            ch = buffer.read(1)
        ch = buffer.read(1)
        while ch != '\n':
            marks = marks + ch
            ch = buffer.read(1)
        if name in diction.keys():
            diction[name] = diction[name] + float(marks)
        else:
            diction[name] = float(marks)
        name = marks = ''
        ch = buffer.read(1)
    diction = sort_dict(diction)
except IOError as e:
    print('Unable to open file:', strerror(e.errno))
    exit(e.errno)

try:
    buffer = open(filein + '_result.txt', 'w')
except IOError as e:
    print('Unable to open file:', strerror(e.errno))
    exit(e.errno)
for k, v in diction.items():
    buffer.write(k + ':' + str(v) + '\n')
buffer.close()
print('File written')
