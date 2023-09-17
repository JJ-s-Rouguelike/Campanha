import splash as ss
import console as cls
import game as gm
import ranking as rk


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
                print('Jogar')
                gm.inicia()
                break
            elif opcao == 2:
                cls.clear()
                print('Configurações')
                break
            elif opcao == 3:
                cls.clear()
                print('Ranking')
                rk.exibir()
                break
            elif opcao == 4:
                cls.clear()
                print('Sair')
                break
            else:
                cls.clear()
                exibirmenu(splash)
                print("Opção inválida. Tente novamente.")

        except ValueError:
            cls.clear()
            exibirmenu(splash)
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
ss.splash_animtion(splash)
exibirmenu(splash)    # precisa de uma primeira chamada
escolhamenu()