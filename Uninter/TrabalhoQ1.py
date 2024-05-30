print("Bem-vindo a Loja do Pedro Henrique")
valor = int(input("Entre com o valor do produto: "))
quantidade = int(input("Entre com a quantidade do produto: "))
res = (valor * quantidade) #base para os ifs

if (res >= 10000):
    desconto = res * (89 / 100) #optei por colocar o valor de 11% - 100 logo no cálculo
    print(f"O valor total SEM desconto: R${res}")
    print(f"O valor total COM desconto: R${desconto}")
elif ((res >= 6000) and (res < 10000)):
    desconto = res * (93 / 100)
    print(f"O valor total SEM desconto: R${res}")
    print(f"O valor total COM desconto: R${desconto}")
elif ((res >= 2500) and (res < 6000)):
    desconto = res * (96 / 100)
    print(f"O valor total SEM desconto: R${res}")
    print(f"O valor total COM desconto: R${desconto}")
elif (res < 2500 and res > 0):
    print(f"O valor total SEM desconto: R${res}")
    print("Não há desconto para esse valor!") #coloquei essa mensagem para aviso ao usuário
else:
    print("Digite um valor maior que zero!")