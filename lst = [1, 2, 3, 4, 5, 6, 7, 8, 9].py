lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sud = input('Enter your sudoku:')
list_sud = []
lrow = []
if len(sud) != 81:
    print('Incorrect Sudoku entered')
    exit()
for ch in sud:
    list_sud.append(int(ch))

for i in range(0, 81, 9):
    lrow.append(list_sud[i:i + 9])

for i in range(9):
    for j in range(9):
        try:
            print(lrow[i][j],end='')
            lst.remove(lrow[i][j])
        except:
            print('Not a Sudoku')
            exit()
    print()
    if len(lst) != 0:
        print('Not a Sudoku')
        exit()
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(9):
    for j in range(9):
        try:
            lst.remove(lrow[j][i])
        except:
            print('Not a Sudoku')
            exit()
    if len(lst) != 0:
        print('Not a Sudoku')
        exit()
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for r in range(0,7,3):
    for c in range(0,7,3):
        for i in range(3):
            for j in range(3):
                try:
                    lst.remove(lrow[r+i][c+j])
                except:
                    print('Not a Sudoku')
                    exit()
        if len(lst) != 0:
            print('Not a Sudoku')
            exit()
        lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print('Sudoku')
