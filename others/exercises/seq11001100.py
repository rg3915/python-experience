c = 1
for i in range(1, 10 + 1):
    print c
    if i % 2 == 0:
        c += 1
    if c % 2 == 0:
        c = 0
