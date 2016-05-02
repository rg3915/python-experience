from random import randint

trials, flips = 10000, 0

for trial in range(trials):
    flips += 1
    if randint(0, 1) == 0:
        while randint(0, 1) == 0:
            flips += 1
        flips += 1
    else:
        while randint(0, 1) == 1:
            flips += 1
        flips += 1

print('Deep analysis of your inquiry produced:', flips / trials)
