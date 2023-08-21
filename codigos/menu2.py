def exibirmenu():
    print('ROGUE')
    print('1. Jogar')
    print('2. Configurações')
    print('3. Progresso')
    print('4. Sair')

def escolhamenu():
    while True:
        exibirmenu()
        try:
            opcao = int(input('Digite a sua opção:'))

            if opcao == 1:
                print('Jogar')
                break
            elif opcao == 2:
                print('Configurações')
                break
            elif opcao == 3:
                print('Progresso')
                break
            elif opcao == 4:
                print('Sair')
                break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Digite um número válido. Tente novamente.")
