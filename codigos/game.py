import mapas as mp
import console as cls
import config as cf
import curses
import random

#import keyboard #Util, mas n gostei

def inicia():
    #cls.clear()
    #a = input("tente fugir do lip 3!")
    curses.wrapper(fase1)

def encontrar_posicoes_validas(mapa):
    posicoes_validas = []

    for i, linha in enumerate(mapa):
        for j, char in enumerate(linha):
            if char == '.':
                posicoes_validas.append((i, j))

    return posicoes_validas

moedas = [] #Lista para as coordenadas das moedas
bats = []
##############################################################################################################################################
def fase1(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)

    #setando os conjuntos de cores
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)  


    posicoes_validas = encontrar_posicoes_validas(mp.mapa1.split('\n'))

    y, x = random.choice(posicoes_validas)

    stdscr.clear()
    stdscr.addstr(0, 0, "Aperte alguma seta e sobreviva!")

    imprimir_ponte_flag = False

#Loop do jogo, definir GameOver

    while True:
        key = stdscr.getch()

# Setas, movimentação
        if key == curses.KEY_UP:
            novo_y, novo_x = max(y-1, 0), x
        elif key == curses.KEY_DOWN:
            novo_y, novo_x = min(y+1, len(mp.mapa1.split('\n'))-2), x
        elif key == curses.KEY_LEFT:
            novo_y, novo_x = y, max(x-1, 0)
        elif key == curses.KEY_RIGHT:
           novo_y, novo_x = y, max(x+1, 0)
 #Golpes          
        elif key == ord('a') or key == ord('A'): #Aqui vai ser um golpe e a condição pra abrir o mapa 2 vai ser: 10g e/ou bats...
            imprimir_ponte_flag = True
            mp.mapa1 = '\n'.join(injetar_ponte(mp.mapa1.split('\n')))
            #posicoes_validas = encontrar_posicoes_validas(mp.mapa1.split('\n'))
        else:
            continue

# Sessãoo de condições especiais do mapa

        if mp.mapa1.split('\n')[novo_y][novo_x] != '#':
            y, x = novo_y, novo_x

        stdscr.clear()
#coins
        if cf.player[3] % cf.rateMoeda == 0 and cf.player[3] != 0:
            posicao_moeda = adicionar_moeda_aleatoria(mp.mapa1.split('\n'))
            if posicao_moeda:
                moedas.append(posicao_moeda)
    #Lógica
        if (y, x) in moedas:
            moedas.remove((y, x))
            cf.player[1] += 1

        #imprimir_moedas(stdscr, moedas)
#coins

#bats   
        if cf.player[3] % cf.rateMorcego == 0 and cf.player[3] != 0:
            posicao_bat = adicionar_bat_aleatorio(mp.mapa1.split('\n'))
            if posicao_bat:
                bats.append(posicao_bat)
        
    #lógica:
        for bat in bats:
            i, j = bat
            if abs(i - y) <= 1 and abs(j - x) <= 1:
                cf.player[4] -= 1  # Remove 1 da vida do jogador
                if cf.player[4] == 0:
                           stdscr.addstr(7, 27, "Você morreu =(")
                           pass
#bats
        desenhar_mapa1(stdscr)
        imprimir_moedas(stdscr, moedas)
        imprimir_bats(stdscr, bats)


        if imprimir_ponte_flag:  # Verifica se a ponte deve ser impressa
            imprimir_ponte(stdscr)
            #imprimir_ponte_flag = False #Debug

        if mp.mapa1.split('\n')[novo_y][novo_x] != '#': #pra restringir
            y, x = novo_y, novo_x
            contar_movimentos()  # Chama a função para contar os movimentos

        # if cf.player[3] % 10 == 0:
        #             adicionar_moedas_aleatorias(mp.mapa1.split('\n'))

        stdscr.addch(y, x, ord(cf.player[0]))
        #stdscr.addch(2, 2, ord('g')) #Debug de gold 
        #stdscr.addstr(2, 3, 'MMMMM') #Debug de mato
        stdscr.addstr(0, 8, "Fuja do lip 3!")
        stdscr.addstr(5, 27, f"Gold: {cf.player[1]}, Vida: {cf.player[4]} Stamina: {cf.player[5]}")
        stdscr.addstr(0, 27, f"Número de Movimentos: {cf.player[3]}, COORDS: {y} e {x}")
        stdscr.refresh()
        #Fim do loop e da função
##############################################################################################################################################


def desenhar_mapa1(stdscr):
    for i, linha in enumerate(mp.mapa1.split('\n')):
        for j, char in enumerate(linha):
            if char == '#':
                stdscr.addch(i, j, ord(char), curses.color_pair(1) | curses.A_DIM)
            else:
                stdscr.addch(i, j, ord(char))

#Exemplo de como poeria ser pra chamar o mapa 2 a partir de 27, 27 e depoi ver como otar uma ponte 

# def desenhar_mapa2(stdscr):
#     for i, linha in enumerate(mp.mapa2.split('\n')):
#         for j, char in enumerate(linha):
#             if char == '#':
#                 stdscr.addch(i+27, j+27, ord(char), curses.color_pair(1) | curses.A_DIM)
#             else:
#                 stdscr.addch(i+27, j+27, ord(char))
# a chamada:
#         desenhar_mapa2(stdscr)

def imprimir_ponte(stdscr):
    ponte = mp.ponteVertical.strip().split('\n')  # Remove espaços extras e divide em linhas

    for i, linha in enumerate(ponte):
        for j, char in enumerate(linha):
            if char == '#':
                stdscr.addch(i+9, j+14, ord(char), curses.color_pair(1))
            else:
                stdscr.addch(i+9, j+14, ord(char))

def injetar_ponte(mapa):
    novo_mapa = mapa.copy()  # Cria uma cópia do mapa original para não modificá-lo diretamente
    ponte = mp.ponteVertical.strip().split('\n')

    for i, linha in enumerate(ponte):
        for j, char in enumerate(linha):
            if i + 9 >= len(novo_mapa):
                novo_mapa.append('.' * len(novo_mapa[0]))  # Adiciona uma nova linha ao mapa se necessário
            if j + 14 >= len(novo_mapa[i + 9]):
                novo_mapa[i + 9] += ' ' * (j + 14 - len(novo_mapa[i + 9]) + 1)  # Adiciona pontos à linha se necessário
            novo_mapa[i + 9] = novo_mapa[i + 9][:j + 14] + char + novo_mapa[i + 9][j + 15:]

    return novo_mapa


def contar_movimentos():
    cf.player[3] += 1

#mp.printMap(mp.mapa1)
#print(cf.player[0])


def adicionar_moeda_aleatoria(mapa):
    posicoes_validas = encontrar_posicoes_validas(mapa)
    if posicoes_validas:
        i, j = random.choice(posicoes_validas)
        mapa[i] = mapa[i][:j] + 'G' + mapa[i][j+1:]
        return (i, j)
    else:
        return None

def imprimir_moedas(stdscr, moedas):
    for moeda in moedas:
        i, j = moeda
        stdscr.attron(curses.color_pair(2))  # Ativa 
        stdscr.addch(i, j, ord('g'))  
        stdscr.attroff(curses.color_pair(2))  # Desativa 

def adicionar_bat_aleatorio(mapa):
    posicoes_validas = encontrar_posicoes_validas(mapa)
    if posicoes_validas:
        i, j = random.choice(posicoes_validas)
        mapa[i] = mapa[i][:j] + 'b' + mapa[i][j+1:]
        return (i, j)
    else:
        return None

def imprimir_bats(stdscr, bats):
    for bat in bats:
        i, j = bat
        stdscr.attron(curses.color_pair(3))  # Ativa a cor azul
        stdscr.addch(i, j, ord('b'))
        stdscr.attroff(curses.color_pair(3))  # Desativa a cor azul
