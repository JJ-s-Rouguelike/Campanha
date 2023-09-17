import mapas as mp
import console as cls
import config as cf
import curses
import random

def inicia():
    cls.clear()
    curses.wrapper(movimento)

def movimento(stdscr):
    curses.curs_set(0) 
    stdscr.nodelay(1) 

    y, x = curses.LINES//2, curses.COLS//2
    stdscr.addch(y, x, cf.player[0]) #dados armazenados na lista de ados do jogador
    
    while True:
        key = stdscr.getch()
    
        if key == curses.KEY_UP:
            y = max(y-1, 0)
        elif key == curses.KEY_DOWN:
            y = min(y+1, curses.LINES-1)
        elif key == curses.KEY_LEFT:
            x = max(x-1, 0)
        elif key == curses.KEY_RIGHT:
            x = min(x+1, curses.COLS-1)

        stdscr.clear()
        stdscr.addch(y, x, cf.player[0])
        stdscr.refresh()


#mp.printMap(mp.mapa1)
#print(cf.player[0])