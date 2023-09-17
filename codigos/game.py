import curses
import mapas as mp
import console as cls
import config as cf

def inicia():
    cls.clear()
    mp.printMap(mp.mapa1)
    a = input("Pressione Enter para summonar...")

