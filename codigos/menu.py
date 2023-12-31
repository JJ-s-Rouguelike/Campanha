import splash as ss
import console as cls
import game as gm
import ranking as rk
import config as cf
import time
import mapas as mp

def exibirmenu(matriz):
    
    ss.splash_estatica(matriz)
    print('\n')
    print('1. Jogar')
    print('2. Configurações')
    print('3. Ranking')
    print('4. Sair')
    print('\n')

def escolhamenu():
    while True:
        
        try:
            opcao = int(input('Digite a sua opção:'))

            if opcao == 1:
                cls.clear()
                gm.bats = []
                gm.moedas = []
                gm.flag1 = False
                gm.flag2 = False
                mp.mapaDegeneration()
                gm.inicia()
                gm.youDied(cf.player[1])
                break

            elif opcao == 2:
                cls.clear()
                exibirConfig(splash)
                escolhaConfig()
                break
            elif opcao == 3:
                cls.clear()
# já tem arqivo e fnc inicializadora
                ss.splash_estatica(splash) #temporário
                rk.exibir()
                loop = input("Aperte enter para voltar.")
                opcao = 0
                cls.clear()
                exibirmenu(splash)   
                escolhamenu()               
                break
            elif opcao == 4:
                cls.clear()
                ss.splash_estatica(splash) #temporário
                print('Até mais!')
                break
            else:
                cls.clear()
                exibirmenu(splash)
                print("Opção inválida. Tente novamente.")

        except ValueError:
            cls.clear()
            exibirmenu(splash)
            print("Digite um número válido. Tente novamente.")

def exibirConfig(matriz):
    
    ss.splash_estatica(matriz)
    print('\n')

    if cf.rateDificuldade == 0:
        print("Dificldade atual: Fácil")
    elif cf.rateDificuldade == 1:
        print("Dificldade atual: Médio")
    else:
        print("Dificldade atual: Difícil")
    
    print('\n')
    print('1. Nivel facil: mais moedas, vida,  // menos bats (eles dão vida), mapas, preciosidade (valor do gold) stamina')
    print('2. Nivel normal: jogo regular')
    print('3. Nivel dificil: menos moedas, vida,  // mais bats, mapas, stamina, preciosidade e névoa!')
    print('4. voltar')
    print('\n')

def escolhaConfig():
    while True:
        
        try:
            opcao = int(input('Digite a sua opção:'))

            if opcao == 1:
                cf.rateDificuldade = 0
                cf.rateMoeda = 5
                cf.rateMorcego = 20

                print("Fácil selecionado")
                time.sleep(3)
                cls.clear()
                exibirmenu(splash)    
                escolhamenu()
                break
            elif opcao == 2:
                cf.rateDificuldade = 1
                cf.rateMoeda = 10
                cf.rateMorcego = 15

                print("Médio selecionado")
                time.sleep(3)
                cls.clear()
                exibirmenu(splash) 
                escolhamenu()
                break
            elif opcao == 3:
                cf.rateDificuldade = 2
                cf.rateMoeda = 15
                cf.rateMorcego = 10

                print("Difícil selecionado")
                time.sleep(3)
                cls.clear()
                exibirmenu(splash) 
                escolhamenu()
                break

            elif opcao == 4:
                cls.clear()
                exibirmenu(splash)    # precisa de uma primeira chamada
                escolhamenu()


                break
            else:
                cls.clear()
                exibirConfig(splash)
                print("Opção inválida. Tente novamente.")

        except ValueError:
            cls.clear()
            exibirConfig(splash)
            print("Digite um número válido. Tente novamente.")


#Chamadas
cls.clear()

splash = [
    "    ##     ##  #    #####       #####   #     #  #     #   #####  ######  #####   #     #",
    "    ##     ##  #   #            #     # #     #  ##    #  #       #      #     #  ##    #",
    "    ##     ##     ######        #     # #     #  # #   #  #  #### #####  #     #  # #   #",
    "#   ## #   ##          #        #     # #     #  #  #  #  #     # #      #     #  #  #  #",
    " ####   ####     ######         #####    #####   #    ##   #####  ######  #####   #    ##"
]
ss.splash_animtion(splash) # animação, vou dexar comentado pa agilizar o debug
exibirmenu(splash)    # precisa de uma primeira chamada
escolhamenu()
