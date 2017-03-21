'''
Problema 1.7 - Dados um número inteiro n >= 0, e uma sequência com n inteiros,
determinar o maior inteiro da sequêcia. Por exemplo, para a sequência
6 -2 7 0 -5 8 4 o programa deve escrever o número 8.

Solução:

'''

i = 0
maior = 0

n = int(input("Insira o tamanho da sequência: "))

for i in range(n):
   numero = int(input("Insira o próximo número: "))
   if numero > maior:
       maior = numero

print("O maior número da sequência é: ", maior)
    
    
