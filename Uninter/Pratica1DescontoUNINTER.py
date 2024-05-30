preco = float(input("Digite o preço do produto: "))
percentual = float(input("Digite o percentual de desconto(0-100%)"))

desconto = preco * (percentual / 100)
final = preco - desconto

print(f"O valor do produto é {preco}. Mais o desconto de {percentual}%")
print(f"O valor calculado de desconto: {desconto}. Valor final do produto: {final}") #exercicio 1

percorrido = float(input("Digite os kilometros percorridos por você: "))
dias = int(input("Digite a quantidade de dias que o veículo está alugado: "))

kmrodado = percorrido * 0.15
aluguel = dias * 60
pagamento = kmrodado + aluguel

print(f"O aluguel do seu carro custou {aluguel}. Com gasolina foram gastos {kmrodado}.")
print(f"Assim o total a pagar será de {pagamento}") #exercicio 2

frase = input("Digite uma frase: ")
tam = len(frase)

frase2 = frase[:int(tam/2)]
print(frase2[-2:]) #exercicio 3. o menos antes dos dois pontos pega os últimos caracteres da frase.