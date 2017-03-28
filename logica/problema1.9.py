'''
Problema 1.9 - Dados um número inteiro n > 0 e uma sequência com n números inteiros,
verificar se a sequência esta em ordem crescente

Solução:
'''

n = int(input("Insira a quantidade de números: "))
crescente = 1
anterior = int(input("Digite o primeiro número: "))

for i in range(n - 1):
    numero = int(input("Digite o próximo número: "))
    if (anterior >= numero):
        crescente = 0
    anterior = numero

if crescente == 1:
    print("A sequência é crescente")
else:
    print("A sequência não é crescente")
