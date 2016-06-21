# principais sintaxes do python
# ---------------------------------------------------------------
# http://www.swaroopch.org/notes/Python_pt-br:Operadores_e_Expressoes
# operadores em Python

# operadores aritmeticos

# ** 	potencia
# // 	divisao inteira	4 // 3 retorna 1
# % 	modulo

# operadores relaconais

# ==	igual
# !=	diferente
# and or not
# ---------------------------------------------------------------
x = int(raw_input('Digite um numero inteiro: '))
if x < 0:
    x = 0
    print 'negativo mudado para zero.'
elif x == 0:
    print 'Zero'
elif x == 1:
    print 'Um'
else:
    print 'Mais'
# ---------------------------------------------------------------
n = 5
soma = 0
print 'Digite 5 numeros.'
for i in range(1, n + 1):
    num = int(raw_input('Numero: '))
    if num > 0:
        soma = soma + num
    else:
        print num, 'eh negativo.'
print 'Total:', soma
# ---------------------------------------------------------------
valor = int(raw_input('Digite o valor que voce deseja sacar: '))
n50 = n20 = n10 = 0
if valor % 10 != 0:
    print 'Valor invalido.'
else:
    while valor >= 10:
        if valor >= 50:
            n50 += 1
            valor -= 50
        else:
            if valor >= 20:
                n20 += 1
                valor -= 20
            else:
                if valor >= 10:
                    n10 += 1
                    valor -= 10
print 'nota de 50 =', n50
print 'nota de 20 =', n20
print 'nota de 10 =', n10
# ---------------------------------------------------------------
# despdom1.py - Calculadora de despesas domesticas
print 'Balanco de despesas domesticas'
Regis = raw_input('Quanto voce gastou? ')
total = float(Regis)
print total
# print 'Gastos por pessoa = R$ %s.' % media
# ---------------------------------------------------------------
print 'Lista de valores:'
lista = [1, 4, 5, 3, 8, 12]
for l in lista:
    print l
# ---------------------------------------------------------------
print 'Vetor:'
v = [5, 4, 2, 3, 8, 7, 6, 8, 10, 12, 14, 16, 17, 15, 200]
for i in range(len(v)):
    if v[i] % 2 == 0:
        print v[i]
# ---------------------------------------------------------------
print 'Exemplo de range: de 0 a 6'
for i in range(7):
    print i
# ---------------------------------------------------------------
print 'Elementos de uma matriz:'
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = [7, 8, 9]
matriz = [l1, l2, l3]
print matriz
print matriz[1]
print matriz[1][2]
# ---------------------------------------------------------------
print 'Vetor alternado'
A = range(5 + 1)
B = range(5 + 1)
C = range(10 + 1)
j = 1
for i in range(1, 10 + 1, 2):
    C[i] = A[j]
    C[i + 1] = -B[j]
    j += 1
for i in range(1, 10 + 1):
    print C[i]
# ---------------------------------------------------------------
# Escreve a sequencia de Fibonacci ate n
# Define uma funcao


def fib(n):
    a, b = 0, 1
    while a < n:
        print a,
        a, b = b, a + b
fib(2000)
# ---------------------------------------------------------------
# inverte numero
n = 45029
i = 0
while n > 0:
    i = i * 10 + n % 10
    n /= 10
print i
