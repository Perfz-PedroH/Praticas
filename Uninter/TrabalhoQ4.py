def valida_int(pergunta, min, max): #Variavel para o input e suas limitações
    x = int(input(pergunta))
    while((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

#Programa Principal
while True:
    print("Menu")
    print("1 - Cadastrar Livro")
    print("2 - Consultar Livro(s)")
    print("3 - Remover Livro")
    print("4 - Sair")

    op = valida_int("Escolha a opção desejada: 1, 2, 3, 4")
    if (op == 1): #novo item
        print("Opção de Cadastrar livro selecionada...")

    elif (op == 2):
        print("Opção de Consultar livro selecionada...")

    elif (op == 3):
        print("Opção de Remover livro selecionada...")