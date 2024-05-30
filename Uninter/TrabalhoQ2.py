print ("Seja bem vindo a loja de gelados do Pedro") 
print ("Cardápio")
print ("---| Tamanho | Cupuaçu(CP) |   Açaí(AC)   |---")
print ("---|    P    |   R$ 9.00   |   R$ 11.00   |---")
print ("---|    M    |   R$ 14.00  |   R$ 16.00   |---")
print ("---|    G    |   R$ 18.00  |   R$ 20.00   |---")

total = 0

while True: #Validando as entradas de sabor e tamanho
    sabor = input("Digite o sabor desejad(CP/AC): ")
    if (sabor != "CP" and sabor != "AC"):
        print("Sabor inválido. Tente novamente!")
        continue

    tamanho = input("Digite o tamanho desejado(P/M/G): ")
    if (tamanho != "P" and tamanho != "M" and tamanho != "G"):
        print("Tamanho inválido. Tente novamente.")
        continue
    
    if sabor == "CP": #repetição + acumulação do tamanho e sabores 
        if tamanho == "P":
            total += 9 #utilizando operador especial para simplificar o code
            print("Você pediu um Cupuaçu tamanho P: 9")

        elif tamanho == "M":
            total += 14
            print("Você pediu um Cupuaçu tamanho M: 14")

        else:
            tamanho == "G"
            total += 18
            print("Você pediu um Cupuaçu tamanho G: 18")

    else:
        if tamanho == "P":
            total += 11
            print("Você pediu um Açaí tamanho P: 11")

        elif tamanho == "M":
            total += 16
            print("Você pediu um Açaí tamanho M: 16")

        else:
            tamanho == "G"
            total += 20
            print("Você pediu um Açaí tamanho G: 20")

    continuar = input("Deseja pedir mais alguma coisa(S/N)? ")

    if continuar != "S":
        print(f"Total do pedido = {total}")
        break