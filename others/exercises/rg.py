n = 403289440
subtotal = 0
total = 0
ml = 0
m = 10
while n > 0:
    resto = n % 10
    n /= 10
    m -= 1
    subtotal = resto * m
    ml += subtotal
    print(resto, m, subtotal)
ml *= 10
total = ml / 11
total *= 11
digito = ml - total
print(digito)
