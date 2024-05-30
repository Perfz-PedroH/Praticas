def desconto(num_paginas): #Começando com as funções
    if (num_paginas < 20):
        return num_paginas
    elif (20 <= num_paginas < 200):
        return num_paginas * 0.85
    elif (200 <= num_paginas < 2000):
        return num_paginas * 0.8
    elif (2000 <= num_paginas < 20000):
        return num_paginas * 0.75
    else:
        return "Número de páginas incorreto!"

def escolha_servico():
    while True:
        try:
            servico = input("Escolha um tipo de serviço:")
            if (servico in ("DIG", "ICO", "IPB", "FOT")):
                return servico
            else:
                print("Escolha inválida, entre com o serviço novamente...")
        except KeyboardInterrupt:
            print("Programa interrompido...")

def num_pagina():
    while True:
        try:
            num_paginas = int(input("Digite um número de páginas: "))
            if (num_paginas >= 20000):
                print("Número de páginas muito alto. Por favor, Digite um valor menor...")
            else:
                return desconto(num_paginas)
        except ValueError:
            print("Oops. Digite um número de páginas válidas.")

def servico_extra():
    while True:
        print("1 - Encadernação Simples - R$ 15.00") #Apresentação dos serviços extras
        print("2 - Encadernação Capa Dura - R$ 40.00")
        print("0 - Não desejo mais nada!")
        try:
            extra = int(input("Digite o número de serviço extra desejado:"))
            if (extra in (1, 2, 0)):
                return extra
            else:
                print("Escolha uma das opções.")
        except ValueError:
            print("Por favor, digite um valor numérico.")

#Programa principal
print ("Seja bem vindo a copiadora do Pedro")

#Serviços apresentados ao usuário
print("Escolha um tipo de serviço:")
print("DIG - Digitalização")
print("ICO - Impressão Colorida")
print("IPB - Impressão Preto e Branco")
print("FOT - Fotocópia")

servico = escolha_servico()
num_pag_desconto = num_pagina()
extra = servico_extra()

if (servico == "DIG"): #Baseado na atividade de descontos
    custo_por_pagina = 1.10
elif (servico == "ICO"):
    custo_por_pagina = 1.00
elif (servico == "IPB"):
    custo_por_pagina = 0.40
else:
    custo_por_pagina = 0.20

total = (custo_por_pagina * num_pag_desconto)

if (extra == 1):
    total += 15
elif (extra == 2):
    total += 40

print("Serviço selecionado:", servico)
print("Número de páginas:", num_pag_desconto)
if (extra == 1):
    print("Servico_extra: Encadernação Simples")
elif (extra == 2):
    print("Servico_extra: Encadernação Capa Dura")
else:
    print("Nenhum serviço extra escolhido")

print(f"Total: R${total} (serviço:{custo_por_pagina} * páginas:{num_pag_desconto} + extra:{extra})")