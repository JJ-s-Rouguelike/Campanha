import splash as ss
import console as cls
import game as gm
import ranking as rk
import config as cf
import time

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
                gm.inicia()
                gm.youDied()
                #time.sleep(5)
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
    print('1. Nivel facil: mais moedas, vida, stamina // menos inimigos, mapas')
    print('2. Nivel normal: jogo regular')
    print('3. Nivel dificil: menos moedas, vida, stamina // mais inimigos, mapas e névoa')
    print('4. voltar')
    print('\n')

def escolhaConfig():
    while True:
        
        try:
            opcao = int(input('Digite a sua opção:'))

            if opcao == 1:
                print("Fácil selecionado")
                time.sleep(3)
                cls.clear()
                exibirmenu(splash)    
                escolhamenu()
                break
            elif opcao == 2:
                print("Médio selecionado")
                time.sleep(3)
                cls.clear()
                exibirmenu(splash) 
                escolhamenu()
                break
            elif opcao == 3:
                print("Fácil selecionado")
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


########################################################################
#chamadas da config
########################################################################
