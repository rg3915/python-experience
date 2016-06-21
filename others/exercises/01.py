n = 5
soma = 0
for i in range(1, n + 1):
    num = int(raw_input('Numero: '))
    if num > 0:
        soma = soma + num
    else:
        print num, 'eh negativo.'
print soma
