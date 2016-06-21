n = 2374
pot = 0
decimal = 0
subtotal = 0
while n > 0:
    resto = n % 8
    n /= 8
    decimal = resto * 8 ^ pot
    pot += 1
    subtotal += decimal
    print subtotal
