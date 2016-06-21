n = int(raw_input('Digite um numero decimal: '))
octal = 0
d = 1
while n > 0:
    resto = n % 8
    n /= 8
    octal += resto * d
    d *= 10
print 'Octal:', octal
