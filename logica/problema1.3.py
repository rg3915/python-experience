'''
Problema 1.3 - Dado um número inteiro n >= 0, calcular n!

n! = 1,       se n = 0
     n,       se n = 1
     n(n-1)!, se n > 1

Solução:
'''
n = int(input("Digite um número: "))
resultado = 1
i = n
while (i >= 1):
	resultado = resultado * i
	i = i - 1
print(resultado)
