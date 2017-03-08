'''
Problema 1.1 - Dada uma sequência de números inteiros diferentes de zero,
terminada por um zero, calcular a sua soma.
Por exemplo, para a sequência 12, 7, 4, -6, 8, 0 o seu programa deve escrever
o número 25 (retificação).

Solução:
'''

soma = 0
numero = int(input())

print(numero)

while (numero != 0):
    soma += numero
    numero = int(input())
    print(numero)

print(soma)
