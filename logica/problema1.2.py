'''Problema 1.2 - Dados os números inteiros n e k com k >= 0, determinar n^k. Por exemplo, dados os números 3 e 4 o programa deve escrever o número 81.

Solução:
'''
n = int(input("Digite um número: "))
k = int(input("Digite outro número: "))
resultado = 1
potencia = 0
while (potencia < k):
	resultado = resultado * n
	potencia = potencia + 1
print(resultado)
