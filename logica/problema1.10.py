'''
Problema 1.10 - Dados números inteiros n, i e j, todos maiores que zero,
imprimir em ordem crescente os n números naturais que são múltiplos de i ou j
ou ambos. Por exemplo, para n = 6, i = 2 e j = 3, a saída deverá ser: 0 2 3 4 6 8

Solução:

'''

atual = multiplos = 0
n = int(input("Digite o valor de n: "))
i = int(input("Digite o valor de i: "))
j = int(input("Digite o valor de j: "))

while(multiplos < n):
    if (atual % i == 0 or atual % j == 0):
        multiplos = multiplos + 1;
        print(atual, " ")
    atual = atual + 1
