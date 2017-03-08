'''
Problema 1.5 - Dados um número inteiro n >= 0, e uma sequência com n inteiros, determinar a soma dos inteiros positivos 
e a soma dos inteiros negativos da sequência. Por exemplo, para a sequência 6 -2 7 0 -5 8 4 o programa deve escrever o número 25 e -7.

Solução:
'''

i = 0
pos = 0
neg = 0
n = int(input("Digite o comprimento da sequência: "))
while(i < n):
	numero = int(input("Digite o próximo número: "))
	if(numero > 0):
		pos = pos + numero
	else:
		neg = neg + numero
	i = i + 1
print("A soma dos inteiros positivos é: ", pos)
print("A soma dos inteiros negativos é: ", neg)
