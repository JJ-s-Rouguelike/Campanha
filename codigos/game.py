import mapas as mp
import console as cls
import config as cf
import curses
import random
import time
from colorama import Fore, Back, Style, init
import ranking as rk
import sys

#import keyboard #Util, mas n gostei

# aqui elas ficam globais
global imprimir_ponte_flag, imprimir_mapa2_flag  # bambiarra pa n er poblema com o mapa degenerar ao normal
imprimir_ponte_flag = False 
imprimir_mapa2_flag = False

flag1 = 0
flag2 = 0

def inicia():
    global imprimir_ponte_flag, imprimir_mapa2_flag 
    #cls.clear()
    #a = input("tente fugir do lip 3!")
    curses.wrapper(fase1)
    cf.player[1] = 0

    if cf.rateDificuldade == 0:
        cf.rateMoeda = 5
        cf.rateMorcego = 20
        cf.player[5] = 5
        cf.player[4] = 10

    elif cf.rateDificuldade == 1:
        cf.rateMoeda = 10
        cf.rateMorcego = 15
        cf.player[5] = 7
        cf.player[4] = 7

    elif cf.rateDificuldade == 2:
        cf.rateMoeda = 15
        cf.rateMorcego = 10
        cf.player[5] = 10
        cf.player[4] = 5


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
    global imprimir_ponte_flag, imprimir_mapa2_flag
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

    # if flag1 == 0:
    #     imprimir_ponte_flag = False
    # if flag2 == 0:
    #     imprimir_mapa2_flag = False


#Loop do jogo, definir GameOver

    while cf.player[4] > 0:
        key = stdscr.getch()

#primeiro de tudo:
        if not moedas:  #caso a lista de moedas fiqu vazia vazia
            posicao_moeda = adicionar_moeda_aleatoria(mp.mapa1.split('\n'))
            if posicao_moeda:
                moedas.append(posicao_moeda)

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
        elif key == (ord('w') or key == ord('W')) and cf.player[5] >= 1: #Aqui vai ser um golpe e a condição pra abrir o mapa 2 vai ser: 10g e/ou bats...
            # imprimir_ponte_flag = True
            # mp.mapa1 = '\n'.join(injetar_ponte(mp.mapa1.split('\n')))
            # #posicoes_validas = encontrar_posicoes_validas(mp.mapa1.split('\n'))
            novo_y, novo_x = max(y-2, 0), x
            cf.player[5] -= 1
            atacar_morcego(novo_y, novo_x)
        elif key == (ord('s') or key == ord('S')) and cf.player[5] >= 1:
            novo_y, novo_x = min(y+2, len(mp.mapa1.split('\n'))-2), x
            cf.player[5] -= 1
            atacar_morcego(novo_y, novo_x)
        elif key == (ord('a') or key == ord('A')) and cf.player[5] >= 1:
            novo_y, novo_x = y, max(x-2, 0)
            cf.player[5] -= 1
            atacar_morcego(novo_y, novo_x)
        elif key == (ord('d') or key == ord('D')) and cf.player[5] >= 1:
           novo_y, novo_x = y, max(x+2, 0)
           cf.player[5] -= 1
           atacar_morcego(novo_y, novo_x)
        else:
            continue

# Sessãoo de condições especiais do mapa


        if (cf.player[1] >= 10) and (cf.rateDificuldade == 1 or cf.rateDificuldade == 2): #PONTE
            imprimir_ponte_flag = True
            mp.mapa1 = '\n'.join(injetar_ponte(mp.mapa1.split('\n')))
            if not imprimir_mapa2_flag:  # Verifica se o mapa 2 ainda não foi impresso
                mp.mapa1 = '\n'.join(injetar_mapa2(mp.mapa1.split('\n')))
                imprimir_mapa2_flag = True  # Define a flag para True após a injeção do mapa 2

        ##if (cf.player[1] >= 10) and (cf.rateDificuldade == 1 or cf.rateDificuldade == 2):

        if mp.mapa1.split('\n')[novo_y][novo_x] != '#':
            y, x = novo_y, novo_x

        posicoes_validas = encontrar_posicoes_validas(mp.mapa1.split('\n'))
        stdscr.clear()
#coins
        if cf.player[3] % cf.rateMoeda == 0: #and cf.player[3] != 0:
            posicao_moeda = adicionar_moeda_aleatoria(mp.mapa1.split('\n'))
            if posicao_moeda:
                moedas.append(posicao_moeda)
        
        if (cf.player[3] % 10 == 0) and (cf.player[3] != 0): #stamina apos turnos
                cf.player[5] += 1
        elif (cf.player[3] % 10 == 0) and (cf.player[3] != 0): #stamina apos moedas
                cf.player[5] += 1

    #Lógica
        if (y, x) in moedas:
            moedas.remove((y, x))
            if cf.rateDificuldade == 0:
                cf.player[1] += 1

            elif cf.rateDificuldade == 1:
                cf.player[1] += 1.5

            elif cf.rateDificuldade == 2:
                cf.player[1] += 2

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
                           curses.endwin()
                           youDied(cf.player[1])
                           #stdscr.addstr(7, 27, "Você morreu =(")
                           #time.sleep(1)
                           pass
                        #    time.sleep(3) #Debug
                        #    break
        
        if bats:  # Verifica se a lista de morcegos não está vazia
            mover_morcegos()

#bats
        desenhar_mapa1(stdscr)
        imprimir_moedas(stdscr, moedas)
        imprimir_bats(stdscr, bats)


        if imprimir_ponte_flag:  # Verifica se a ponte deve ser impressa
            imprimir_ponte(stdscr)
            #imprimir_ponte_flag = False #Debug
            imprimir_mapa2(stdscr)

        if mp.mapa1.split('\n')[novo_y][novo_x] != '#': #pra restringir
            y, x = novo_y, novo_x
            contar_movimentos()  # Chama a função para contar os movimentos

        # if cf.player[3] % 10 == 0:
        #             adicionar_moedas_aleatorias(mp.mapa1.split('\n'))

        stdscr.addch(y, x, ord(cf.player[0]))
        #stdscr.addch(2, 2, ord('g')) #Debug de gold 
        #stdscr.addstr(2, 3, 'MMMMM') #Debug de Mist
        if cf.rateDificuldade == 2:
            nevoa1(stdscr)
        if (cf.player[1] >= 10) and (cf.rateDificuldade == 1 or cf.rateDificuldade == 2):
            nevoa2(stdscr)

        stdscr.addstr(0, 0, "Fuja do lip 3!")
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

#####

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
    height, width = stdscr.getmaxyx()  # Obtém as dimensões da tela
    for bat in bats:
        i, j = bat
        if 0 <= i < height and 0 <= j < width:  # Verifica se a posição está dentro dos limites da tela
            stdscr.attron(curses.color_pair(3))
            stdscr.addch(i, j, ord('b'))
            stdscr.attroff(curses.color_pair(3))


def youDied(ouro):
    die = [
        " #     #  #######  #     #           ######      #     #######  ######",
        " #     #  #     #  #     #           #     #     #     #        #     #",
        " #######  #     #  #     #           #     #     #     ####     #     #",
        "       #  #     #  #     #           #     #     #     #        #     #",
        " #######  #######  #######           ######      #     #######  ######"
    ]
    #ouro = cf.player[1]
    height = len(die)
    width = len(die[0])

    for colunas in range(1, width+1):
        for i in range(height):
            linha = ""
            for j in range(colunas):
                linha += die[i][j]
            print(Fore.RED + linha + Style.DIM)
        
        time.sleep(0.05)
        cls.clear()

    for linha in die:
        print(Fore.RED + linha + Style.DIM)

    # Esperar 5 segundos
    time.sleep(1)
    rk.nome = input("\nDigite seu nome: ")
    rk.salvar_ranking(rk.nome, cf.rateDificuldade, cf.player[3], ouro)
    print("Adicionado ao mural de Formados!")
    time.sleep(1)
    sys.exit()


    
def injetar_mapa2(mapa):
    novo_mapa = mapa.copy()
    mapa2 = mp.mapa2.strip().split('\n')

    for i, linha in enumerate(mapa2):
        for j, char in enumerate(linha):
            if i + 13 >= len(novo_mapa):
                novo_mapa.append('.' * len(novo_mapa[0]))
            if j >= len(novo_mapa[i + 13]):
                novo_mapa[i + 13] += ' ' * (j - len(novo_mapa[i + 13]) + 1)
            novo_mapa[i + 13] = novo_mapa[i + 13][:j] + char + novo_mapa[i + 13][j + 1:]

    return novo_mapa


def imprimir_mapa2(stdscr):
    mapa2 = mp.mapa2.strip().split('\n')
    stdscr.addstr(22, 0, "não há escapatória.")
    for i, linha in enumerate(mapa2):
        for j, char in enumerate(linha):
            if char == '#':
                stdscr.addch(i+13, j, ord(char), curses.color_pair(1))
            else:
                stdscr.addch(i+13, j, ord(char))


    imprimir_moedas(stdscr, moedas)  # Adicione esta linha
    imprimir_bats(stdscr, bats)
    stdscr.refresh()


def mover_morcegos():
    for i in range(len(bats)):
        direcao = random.choice(['esquerda', 'cima', 'baixo', 'direita', 'cima', 'baixo'])  # Prioriza esquerda e direita

        if direcao == 'cima':
            novo_bat = (max(bats[i][0]-1, 0), bats[i][1])
        elif direcao == 'baixo':
            novo_bat = (min(bats[i][0]+1, len(mp.mapa1.split('\n'))-2), bats[i][1])
        elif direcao == 'esquerda':
            novo_bat = (bats[i][0], max(bats[i][1]-1, 0))
        elif direcao == 'direita':
            novo_bat = (bats[i][0], min(bats[i][1]+1, len(mp.mapa1.split('\n')[0])-1))

        if mp.mapa1.split('\n')[novo_bat[0]][novo_bat[1]] == '.':  # Verifica se a nova posição é válida
            bats[i] = novo_bat

def atacar_morcego(y, x):
    global bats

    for i, (bat_y, bat_x) in enumerate(bats):
        if abs(bat_y - y) <= 1 and abs(bat_x - x) <= 1:
            bats.pop(i)
            if cf.rateDificuldade == 0:
                cf.player[4] += 1.5  # Aumenta a vida em 1.5

    return bats

def nevoa1(stdscr):
    stdscr.addstr(2, 3, 'MMMMM')
    stdscr.addstr(4, 13, 'MMMM')
    stdscr.addstr(8, 2, 'MMMMMM')

def nevoa2(stdscr):
    stdscr.addstr(20, 3, 'MMMMM')
    stdscr.addstr(16, 7, 'MMMM')
    stdscr.addstr(20, 14, 'MMMMMM')
    