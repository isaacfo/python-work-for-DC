

x = int(input('Width?: '))
y = int(input('Height?: '))
rows = 0
cols = 0 
while rows < y: 
    while cols < x:
        if cols == 0 or cols == (x - 1):
            print('* ', end='')
        elif rows > 0 and rows < (y - 1): 
            print('  ', end='')
        else: 
            print("* ", end='')
        cols = cols + 1
    rows = rows + 1
    cols = 0 
    print()