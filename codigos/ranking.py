import console as cls

nome = []

def salvar_ranking(nome, dificuldade, movimentos, ouro):
    with open('ranking.txt', 'a') as arquivo:
        arquivo.write(f'{nome},{dificuldade},{movimentos},{ouro}\n')


def exibir():
    ranking = []
    print("\n\no Os formdos são...\n")
    try:
        with open('ranking.txt', 'r') as arquivo:
            dados = [linha.strip().split(',') for linha in arquivo]
        
        # Ordena os dados pelo ouro em ordem decrescente
        dados_ordenados = sorted(dados, key=lambda x: int(x[3]), reverse=True)

        # Imprime o cabeçalho
        print("{:<20} {:<10} {:<15} {:<15}".format("Nome", "Dificuldade", "Movimentos", "Ouro")) #equivalnte ao printf de Clang
        print("\n")
        for i, dado in enumerate(dados_ordenados[:10]):
            nome, dificuldade, movimentos, ouro = dado
            # Converte o valor da dificuldade para o nome correspondente
            dificuldade = ["Fácil", "Médio", "Difícil"][int(dificuldade)] #não entendi a dessa estrutura, mas acho ue funcionou

            ranking.append(dado)
            print("{:<20} {:<10} {:<15} {:<15}".format(nome, dificuldade, movimentos, ouro))
    except FileNotFoundError:
        print("Seja o primeiro a se formar!")

    return ranking



