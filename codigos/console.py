
import os


clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


def init(lines):
    clear()
    print('\n' * lines, end='', flush=True)

def initAll():
    ts = os.get_terminal_size()
    init(ts.lines)
    print(ts.lines, ts.columns)
    

def reset(x,y,lines,columns):
    gotoxy(x,y)
    for _ in range(lines):
        print(' ' * columns)


def gotoxy(x,y):

    if os.name in ('nt', 'dos'):
        print("%c[%d;%df" % (0x1B, y, x), end='', flush=True)
    else:
        print("%c[%d;%df" % (0x1B, y, x), end='', flush=True)



