from collections import Counter

# Listas para armazenar os dados
filmes = []
anos = []
gens = []
notas = []
avaliacoes = []

def cadastrar_filmes():
    filme = input('Nome do filme: ')
    gen = input('Gênero: ')

    while True:
        try:
            nota = float(input('Nota (0 a 10): '))
            if 0 <= nota <= 10:
                if nota < 4:
                    avaliacoes.append('Ruim')
                elif nota <= 7:
                    avaliacoes.append('Regular')
                elif nota <= 9:
                    avaliacoes.append('Bom')
                else:
                    avaliacoes.append('Ótimo')
                break
            else:
                print("Nota fora do intervalo permitido. Tente novamente.")
        except ValueError:
            print("Valor inválido. Insira um número entre 0 e 10.")

    while True:
        try:
            ano = int(input('Ano de lançamento: '))
            break
        except ValueError:
            print("Ano inválido. Tente novamente.")

    filmes.append(filme)
    anos.append(ano)
    gens.append(gen)
    notas.append(nota)

def listar_filmes():
    if len(filmes) == 0:
        print('Nenhum filme cadastrado.')
    else:
        for i in range(len(filmes)):
            print(f'{i+1}. Nome: {filmes[i]} - Gênero: {gens[i]} - Nota: {notas[i]} - Avaliação: {avaliacoes[i]}')

def buscar_filmes():
    filmes_busca = input("Insira o nome do filme: ")
    encontrado = False
    for i in range(len(filmes)):
        if filmes[i].lower() == filmes_busca.lower():
            print(f'{i+1}. Nome: {filmes[i]} - Gênero: {gens[i]} - Nota: {notas[i]} - Avaliação: {avaliacoes[i]}')
            encontrado = True
            break
    if not encontrado:
        print('Esse filme não foi encontrado.')

def remover_filme():
    filme_remover = input("Digite o nome do filme a ser removido: ").strip()
    if filme_remover in filmes:
        indice = filmes.index(filme_remover)
        filmes.pop(indice)
        anos.pop(indice)
        gens.pop(indice)
        notas.pop(indice)
        avaliacoes.pop(indice)
        print(f'O filme "{filme_remover}" foi removido com sucesso!\n')
    else:
        print(f'O filme "{filme_remover}" não foi encontrado na lista.\n')

def exibir_estatisticas():
    if len(filmes) == 0:
        print("Nenhum filme cadastrado para exibir estatísticas.")
        return

    # qntd de filmes
    total_filmes = len(filmes)

    # media das notas
    media_notas = sum(notas) / total_filmes

    # genero mais cadastrado
    genero_mais_comum = Counter(gens).most_common(1)[0][0]

    # filmes cm notas maiores que 8
    filmes_acima_8 = [filme for filme, nota in zip(filmes, notas) if nota > 8]

    print("\nEstatísticas:")
    print(f"Total de filmes cadastrados: {total_filmes}")
    print(f"Média das notas: {media_notas:.2f}")
    print(f"Gênero mais cadastrado: {genero_mais_comum}")
    print(f"Filmes com notas maiores que 8: {', '.join(filmes_acima_8) if filmes_acima_8 else 'Nenhum'}")

def menu():
    print("\nMenu:")
    print("-" * 50)
    print("1 - Cadastrar filme")
    print("-" * 50)
    print("2 - Listar filmes")
    print("-" * 50)
    print("3 - Buscar filme")
    print("-" * 50)
    print("4 - Remover filme")
    print("-" * 50)
    print("5 - Exibir estatísticas")
    print("-" * 50)
    print("6 - Sair")
    print("-" * 50)

def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            cadastrar_filmes()
        elif opcao == "2":
            listar_filmes()
        elif opcao == "3":
            buscar_filmes()
        elif opcao == "4":
            remover_filme()
        elif opcao == "5":
            exibir_estatisticas()
        elif opcao == "6":
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

if __name__ == "__main__":
    main()


    