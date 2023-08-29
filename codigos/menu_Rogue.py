import ranking as rk
import game
import os
import console as cls

def exibirmenu():
    print("\tAqui vem a splash\n")
    print('1. Jogar')
    print('2. Configurações')
    print('3. Ranking')
    print('4. Sair')

def escolhamenu():
    while True:
        
        try:
            opcao = int(input('Digite a sua opção:'))

            if opcao == 1:
                cls.clear()
                print('Jogar')
                game.inicia()
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
                exibirmenu()
                print("Opção inválida. Tente novamente.")

        except ValueError:
            cls.clear()
            exibirmenu()
            print("Digite um número válido. Tente novamente.")

#Chamadas
cls.clear()
exibirmenu()    # precisa de ua primeira chamada
escolhamenu()