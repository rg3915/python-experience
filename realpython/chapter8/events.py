from random import randint

heads, tails = 0, 0

for trial in range(10000):
    while randint(0, 1) == 0:
        tails += 1
    heads += 1

print('heads / tails = ', heads / tails)
