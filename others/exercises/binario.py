n = 50
binario = 0
potencia = 1
while n > 0:
    digito = n % 2
    print digito
    n = n / 2
    binario = binario + digito * potencia
    potencia = potencia * 10
print binario
