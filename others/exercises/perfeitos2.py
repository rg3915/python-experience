# perfeitos.py
num = int(raw_input('Digite um numero: '))
teste = 0
for n in range(2, num + 1):
    for d in range(1, n):
        if n % d == 0:
            teste = teste + d
    if teste == n:
        print n
    teste = 0
