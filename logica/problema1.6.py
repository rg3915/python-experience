'''
Problema 1.6 - Dados um numero inteiro n >= 0, e uma sequência com n inteiros,
determinar quantos números da sequência são pares e quantos são ímpares. Por
exemplo, para a sequência 6 -2 7 0 -5 8 4 o programa deve escrecer o número 4
para o número de pares e 2 para o número de ímpares.

Solução:

'''
i = 0
pares = 0
impares = 0
n = int(input("Digite o comprimento da sequência: "))

while i < n:
    numero = int(input("Digite o próximo número: "))
    if (numero % 2) == 0:
        pares = pares + 1
    else:
        impares = impares + 1
    i = i + 1

print("Quantidade de pares: ", pares)
print("Quantidade de ímpares: ", impares)
