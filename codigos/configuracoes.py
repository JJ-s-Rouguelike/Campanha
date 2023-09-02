class Configuracao:
    def Configuraçoes_padroes(Padrão):
        Padrão.dificuldade = 'médio'  
        Padrão.resolução = '800x600'  
        Padrão.volume_música = 50  
        Padrão.música_habilitada = True  

    def mostrar_configuracoes(Padrão):
        print("Configurações do Jogo:")
        print(f"Dificuldade: {Padrão.dificuldade}")
        print(f"Resolução: {Padrão.resolução}")
        print(f"Volume da Música: {Padrão.volume_música}")
        print(f"Música: {'Habilitada' if Padrão.música_habilitada else 'Desabilitada'}")

    # (Padrão) pode ser substituido por (self), comumente utilizado em Python. #