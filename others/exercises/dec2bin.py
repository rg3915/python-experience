n = int(raw_input('Digite um numero decimal: '))
bin = 0
d = 1
while n > 0:
    n /= 2
    bin += (n % 2) * d
    d *= 10
print 'bin:', bin
