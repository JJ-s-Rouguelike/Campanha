import console as cls
import os
import random

def inicia():
    cls.clear()
    print('Bem vindo ao Inferno' )
    print('Sobreviva!')

WIDTH = 10
HEIGHT = 10
player = [0, 0]
exit = [WIDTH-1, HEIGHT-1]
enemy = [random.randint(0, WIDTH-1), random.randint(0, HEIGHT-1)]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_board():
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if [x, y] == player:
                print('@', end='')
            elif [x, y] == exit:
                print('E', end='')
            elif [x, y] == enemy:
                print('X', end='')
            else:
                print('.', end='')
        print()

def move(direction):
    if direction == 'w' and player[1] > 0:
        player[1] -= 1
    elif direction == 's' and player[1] < HEIGHT - 1:
        player[1] += 1
    elif direction == 'a' and player[0] > 0:
        player[0] -= 1
    elif direction == 'd' and player[0] < WIDTH - 1:
        player[0] += 1

def move_enemy():
    dx = player[0] - enemy[0]
    dy = player[1] - enemy[1]
    if abs(dx) > abs(dy):
        if dx > 0:
            enemy[0] += 1
        elif dx < 0:
            enemy[0] -= 1
    else:
        if dy > 0:
            enemy[1] += 1
        elif dy < 0:
            enemy[1] -= 1

def main():
    while True:
        clear_screen()
        draw_board()

        if player == exit:
            print("Você ganhou!")
            break
        if player == enemy:
            print("Você perdeu!")
            break

        direction = input("Mova-se com W, A, S, D: ").lower()
        move(direction)
        move_enemy()

main()