import time
import os

def splash_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("+------------------------------------------------+")
    print("|              BEM VINDO AO INFERNO!             |")
    print("|                                                |")
    print("|               Um Jogo Roguelike                |")
    print("|                                                |")
    print("|       Aperte qualquer tecla para jogar         |")
    print("+------------------------------------------------+")
    
    input()

def main():
    splash_screen()
    # Aqui começa o código principal do seu jogo
    print("BEM-VINDO AO INFERNO!")
    # ...

if __name__ == "__main__":
    main()

