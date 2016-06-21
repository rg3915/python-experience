# perfeitos.py
n = int(raw_input('Digite um numero: '))
teste = 0
for i in range(1, n):
    if n % i == 0:
        teste = teste + i
if teste == n:
    print n, 'eh um numero perfeito.'
else:
    print n, 'nao eh um numero perfeito'
