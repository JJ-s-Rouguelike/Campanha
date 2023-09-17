import os
import time
import console as cls

def splash_animtion(matriz):
    height = len(matriz)
    width = len(matriz[0])

    def imprimir_caracteres(colunas):
        for i in range(height):
            linha = ""
            for j in range(colunas):
                linha += matriz[i][j]
            print(linha)

    for colunas in range(1, width+1):
        imprimir_caracteres(colunas)
        time.sleep(0.05)
        cls.clear()



def splash_estatica(matriz):
    for linha in matriz:
        print(linha)