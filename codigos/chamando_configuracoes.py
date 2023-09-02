def menu_configuracao(config):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        config.mostrar_configuracoes()

        print("\nMenu de Configuração:")
        print("1. Alterar Dificuldade")
        print("2. Alterar Resolução")
        print("3. Alterar Volume da Música")
        print("4. Habilitar/Desabilitar Música")
        print("5. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            dificuldades = ["fácil", "médio", "difícil"]
            for idx, dificuldade in enumerate(dificuldades, 1):
                print(f"{idx}. {dificuldade}")
            escolha = input("Selecione a dificuldade: ")
            if escolha in ["1", "2", "3"]:
                config.dificuldade = dificuldades[int(escolha) - 1]

        elif opcao == "2":
            resolucoes = ["800x600", "1024x768", "1920x1080"]
            for idx, resolucao in enumerate(resolucoes, 1):
                print(f"{idx}. {resolucao}")
            escolha = input("Selecione a resolução: ")
            if escolha in ["1", "2", "3"]:
                config.resolucao = resolucoes[int(escolha) - 1]

        elif opcao == "3":
            volume = input("Defina o volume (0-100): ")
            if volume.isdigit() and 0 <= int(volume) <= 100:
                config.volume_musica = int(volume)

        elif opcao == "4":
            config.musica_habilitada = not config.musica_habilitada

        elif opcao == "5":
            break

if __name__ == "__main__":
    import os

    config = Configuracao()
    menu_configuracao(config)
    
    # Chamada da configuracoes.py pro código main (ROGUE ou menu)
    # Feito pelo ChatGPT, sem nenhuma alteração.