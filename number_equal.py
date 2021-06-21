"""
You are given two arrays a1,a2,…,an and b1,b2,…,bn. In each step, you can set ai=ai−bi if ai≥bi. Determine the
minimum number of steps that are required to make all a's equal.

Input format
First line: n
Second line: a1,a2,…,an
Third line: b1,b2,…,bn

Output format
Print the minimum number of steps that are required to make all a's equal. If it is not possible, then print -1.
"""


def sub(a, b):
    count = j = 0
    while j < len(a):
        mini = min(a)
        while a[j] > mini:
            a[j] -= b[j]
            count += 1
        if a[j] < mini:
            mini = a[j]
            j = 0
        else:
            j = j + 1
    for j in range(n):
        assert a[j] > 0, 'No Solution'
    return count


n = int(input('Enter number of numbers:'))
a1 = []
b1 = []
for i in range(n):
    a1.append(int(input('Enter A\'s' + str(i + 1) + ' Number:')))
for i in range(n):
    b1.append(int(input('Enter B\'s' + str(i + 1) + ' Number:')))
for i in range(n):
    assert a1[i] > b1[i], 'Invalid Input'
print(sub(a1, b1))