'''
Problema 1.4 - Dados um número inteiro n >= 0, e uma sequência com n inteiros,
determinar a soma dos inteiros positivos da sequência. Por exemplo, para
a sequência 6, -2, 7, 0, -5, 8, 4 o programa deve escrever o número 25.

Note que no exemplo n = 6. E a sequencia é -2, 7, 0, -5, 8, 4.

Solução:
'''

n = int(input("Digite o comprimento da sequência: "))
contador = 0
soma = 0
while contador < n:
    numero = int(input("Digite o próximo número: "))
    if numero > 0:
        soma = soma + numero
    contador = contador + 1
print("A soma dos inteiros positivos é", soma)
