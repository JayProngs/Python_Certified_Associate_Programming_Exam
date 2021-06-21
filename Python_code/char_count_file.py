from os import strerror


def sort_dict(d):
    return dict(sorted(d.items(), key=lambda item: item[1], reverse=1))


file = input('Enter filename:')  #paas text as input
file=file
dictionary = {}
strng=''
try:
    buffer = open(file+'.txt', 'rt')
except IOError as e:
    print('Unable to open : ', strerror(e.errno))
    exit(e.errno)
for ch in buffer.read():
    if ch != '\n':
        if ch in dictionary.keys():
            val = dictionary[ch]
            dictionary[ch] = val + 1
        else:
            dictionary[ch] = 1

dictionary = sort_dict(dictionary)

for k, v in dictionary.items():
    strng = strng + k + '->' + str(v) + '\n'

file=file+'_hist'
try:
    writeto=open(file+'.txt','w')
except IOError as e:
    print('Unable to open :',strerror(e.errno))
    exit(e.errno)

writeto.write(strng)
writeto.close()
print('File written Successfully')