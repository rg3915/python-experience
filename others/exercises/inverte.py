# inverte numero
n = 45029
i = 0
while n > 0:
    i = i * 10 + n % 10
    n /= 10
print i
