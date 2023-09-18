import mapas as mp
import console as cls
import config as cf
import curses
import random
import keyboard

def inicia():
    #cls.clear()
    #a = input("tente fugir do lip 3!")
    curses.wrapper(movimento)

def encontrar_posicoes_validas(mapa):
    posicoes_validas = []

    for i, linha in enumerate(mapa):
        for j, char in enumerate(linha):
            if char == '.':
                posicoes_validas.append((i, j))

    return posicoes_validas

def movimento(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)

    # Configurando cores
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)

    posicoes_validas = encontrar_posicoes_validas(mp.mapa1.split('\n'))

    y, x = random.choice(posicoes_validas)

    stdscr.clear()
    stdscr.addstr(0, 0, "Aperte alguma seta e sobreviva!")
    while True:
        key = stdscr.getch()

        if key == curses.KEY_UP:
            novo_y, novo_x = max(y-1, 0), x
        elif key == curses.KEY_DOWN:
            novo_y, novo_x = min(y+1, len(mp.mapa1.split('\n'))-2), x
        elif key == curses.KEY_LEFT:
            novo_y, novo_x = y, max(x-1, 0)
        elif key == curses.KEY_RIGHT:
           novo_y, novo_x = y, max(x+1, 0)
        else:
            continue

        if mp.mapa1.split('\n')[novo_y][novo_x] != '#':
            y, x = novo_y, novo_x

        stdscr.clear()

        desenhar_mapa1(stdscr)
        contar_movimentos()

        stdscr.addch(y, x, ord(cf.player[0]))
        stdscr.addstr(0, 8, "FASE 1")
        stdscr.addstr(0, 27, f"Número de Movimentos: {cf.player[3]}, em {y} e {x}")
        stdscr.refresh()


def desenhar_mapa1(stdscr):
    for i, linha in enumerate(mp.mapa1.split('\n')):
        for j, char in enumerate(linha):
            if char == '#':
                stdscr.addch(i, j, ord(char), curses.color_pair(1) | curses.A_DIM)
            else:
                stdscr.addch(i, j, ord(char))

def contar_movimentos():
    cf.player[3] += 1

#mp.printMap(mp.mapa1)
#print(cf.player[0])