atividades = []


def criar_atividades():
    quantidade = int(input('Quantas atividades deseja criar? '))

    for i in range(quantidade):
        atividade = input(f'Digite a atividade {i+1}: ')
        atividades.append([atividade, 0])


def concluir_atividade():
    listar_atividades()
    posatividade = int(input('Digite a posicao da atividade: '))
    atividades[posatividade - 1][1] = 1


def listar_atividades():
    for atividade in atividades:
        if atividade[1] == 0:
            print(f'- {atividade}')


def menu():
    while True:
        print('Menu:')
        print('1. Criar atividade')
        print('2. Listar atividades')
        print('3. Concluir atividade')
        print('4. Sair')

        opcao = input('Digite uma opçao: ')

        while opcao not in ('1', "2", '3', '4'):
            opcao = input('Digite uma opçao: ')

        if opcao == "1":
            criar_atividades()

        elif opcao == "2":
            listar_atividades()

        elif opcao == "3":
            concluir_atividade()

        elif opcao == "4":
            print('Saindo')
            break

        else:
            print('Digite uma opção valida.')


menu()