from colorama import Fore, Style, init

def printMap(mapa): #função para debug
    init(autoreset=True)  # Inicia o colorama

    for linha in mapa.split('\n'):
        for caractere in linha:
            if caractere == '#':
                print(Fore.RED + Style.DIM + '#', end='')
            else:
                print(caractere, end='')

        print()



#COleção de mapas

mapa1 = '''
#########################
#.........#.............#
#.#######.#.#######.###.#
#.#.......#.......#.#...#
#.#######.#.#######.#.#.#
#.#.......#.......#...#.#
#.#######.#.###########.#
#...........#...........#
#########################
'''

mapa2 = '''
#########################
#.........#.............#
#.#####.####.######.###.#
#.#...............###...#
#.#######.#.#######.#.#.#
#.#.......#.......#...#.#
#.#######.#.##.########.#
#...........#...........#s
#########################
'''

mapa3 = '''
#########################
#.......................#
#.#######.#.#######.###.#
#.#.......#.......#.#...#
#............###........#
#............###........#
#.#######.#.###########.#
#...........#...........#
#########################
'''

ponteVertical = '''
#.#
#.#
#.#
#.#
'''