def splash():  

    largura = 50

    def borda():
        print('+' + '-' * (largura-2) + '+')

    def splashcentralizada(texto):
        espaço_total = largura - 2 - len(texto)
        espaço_esquerda = espaço_total // 2
        espaço_direita = espaço_total - espaço_esquerda
        print('|' + ' ' * espaço_esquerda + texto + ' ' * espaço_direita + '|')

    borda()
    splashcentralizada('BEM VINDO AO INFERNO!')
    splashcentralizada('')
    splashcentralizada('')
    splashcentralizada('PRESSIONE ENTER PARA COMEÇAR')
    splashcentralizada('')
    splashcentralizada('')
    splashcentralizada('BOA SORTE, AVENTUREIRO.') 
    borda()

splash()

# Splash Screen básica e inicial, podemos pensar mais sobre ela depois #