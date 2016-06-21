#cpf = 111444777
cpf = 217065018
n = cpf
subtotal = 0
total = 0
m = 1
resto = 0
while n > 0:
    resto = n % 10
    n /= 10
    m += 1
    subtotal = resto * m
    total += subtotal
    print resto, m, subtotal
total %= 11

if total < 2:
    d1 = 0
else:
    d1 = 11 - total

cpf = cpf * 10 + d1
n = cpf

subtotal = 0
total = 0
m = 1
resto = 0
while n > 0:
    resto = n % 10
    n /= 10
    m += 1
    subtotal = resto * m
    total += subtotal
    print resto, m, subtotal
total %= 11


if total < 2:
    d2 = 0
else:
    d2 = 11 - total

print d1, d2
