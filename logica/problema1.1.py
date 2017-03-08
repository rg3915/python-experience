'''
Problema 1.1 - Dada uma sequência de números inteiros diferentes de zero, terminada por um zero, calcular a sua soma. 
Por exemplo, para a sequência 1274-680 o seu programa deve escrever o número 35.

Solução:
'''
soma = 0
numero = int(input())
print(numero) 
while (numero != 0):
	soma = soma + numero
	numero = int(input())
	print(numero)
print(soma)
