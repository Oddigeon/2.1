x1 = int(input())
x2 = int(input())
x3 = int(input())

if x1 > x2 and x1 > x3:
    if x2 > x3:
        print(f'{'Петя':>14}\n{'Вася':>6}\n{'Толя':>22}')
    else:
        print(f'{'Петя':>14}\n{'Толя':>6}\n{'Вася':>22}')
elif x2 > x1 and x2 > x3:
    if x1 > x3:
        print(f'{'Вася':>14}\n{'Петя':>6}\n{'Толя':>22}')
    else:
        print(f'{'Вася':>14}\n{'Толя':>6}\n{'Петя':>22}')
else:
    if x1 > x2:
        print(f'{'Толя':>14}\n{'Петя':>6}\n{'Вася':>22}')
    else:
        print(f'{'Толя':>14}\n{'Вася':>6}\n{'Петя':>22}')

print(f'{'II':^8}{'I':^8}{'III':^8}')