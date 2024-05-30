#Exercício 2: Escreva um algoritmo que leia um valor e que imprima a quantidade de cédulas necessárias para pagar esse mesmo valor. Para simplicar, vamos trabalhar apenas com valores inteiros e com cédulas de R 100,R 50, R 20,R 10, R 5,R 1
valor = int(input("Digite um valor em R$: "))

while True:
  if (valor >= 100):
    cont100 = valor // 100 #para pegar as casas inteiras da divisão
    valor = valor - cont100 * 100
    print(f"Cédulas de 100 são: {cont100}")
    if not valor:
      break

  if (valor >= 50):
    cont50 = valor // 50 
    valor = valor - cont50 * 50
    print(f"Cédulas de 50 são: {cont50}")
    if not valor:
      break

  if (valor >= 20):
    cont20 = valor // 20 
    valor = valor - cont20 * 20
    print(f"Cédulas de 20 são: {cont20}")
    if not valor:
      break

  if (valor >= 10):
    cont10 = valor // 10 
    valor = valor - cont10 * 10
    print(f"Cédulas de 10 são: {cont10}")
    if not valor:
      break

  if (valor >= 5):
    cont5 = valor // 5 
    valor = valor - cont5 * 5
    print(f"Cédulas de 5 são: {cont5}")
    if not valor:
      break

  if (valor >= 2):
    cont2 = valor // 2
    valor = valor - cont2 * 2
    print(f"Cédulas de 2 são: {cont2}")
    if not valor:
      break

  if valor:
    cont1 = valor
    print(f"Cédulas de 1 são: {cont1}")
    break 