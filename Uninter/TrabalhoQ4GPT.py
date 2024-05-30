def cadastrar_livro(id):
    nome = input("Digite o nome do livro: ")
    autor = input("Digite o autor do livro: ")
    editora = input("Digite a editora do livro: ")
    livro = {'id': id, 'nome': nome, 'autor': autor, 'editora': editora}
    lista_livro.append(livro)

def consultar_livro():
    while True:
        try:
            print("Opções de consulta:")
            print("1. Consultar Todos")
            print("2. Consultar por Id")
            print("3. Consultar por Autor")
            print("4. Retornar ao menu")

            opcao = int(input("Escolha uma opção: "))

            if opcao == 1:
                if not lista_livro:
                    print("Nenhum livro cadastrado.")
                else:
                    for livro in lista_livro:
                        print(livro)
            elif opcao == 2:
                id_consulta = int(input("Digite o ID do livro a ser consultado: "))
                for livro in lista_livro:
                    if livro['id'] == id_consulta:
                        print(livro)
            elif opcao == 3:
                autor_consulta = input("Digite o autor do livro a ser consultado: ")
                for livro in lista_livro:
                    if livro['autor'] == autor_consulta:
                        print(livro)
            elif opcao == 4:
                return
            else:
                print("Opção inválida.")
        except ValueError:
            print("Por favor, digite um número.")

def remover_livro():
    try:
        id_remover = int(input("Digite o ID do livro a ser removido: "))
        for livro in lista_livro:
            if livro['id'] == id_remover:
                lista_livro.remove(livro)
                print("Livro removido com sucesso.")
                return
        print("ID inválido.")
    except ValueError:
        print("Por favor, digite um número.")

#Programa Principal
print("Bem-vindo a Livraria do Pedro!")

lista_livro = []
id_global = 0

while True:
    try:
        print("Menu:")
        print("1. Cadastrar Livro")
        print("2. Consultar Livro")
        print("3. Remover Livro")
        print("4. Encerrar Programa")

        opcao_menu = int(input("Escolha uma opção: "))

        if opcao_menu == 1:
            id_global += 1
            cadastrar_livro(id_global)
        elif opcao_menu == 2:
            consultar_livro()
        elif opcao_menu == 3:
            remover_livro()
        elif opcao_menu == 4:
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida.")
    except ValueError:
        print("Por favor, digite um número.")
