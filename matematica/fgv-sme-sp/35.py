# 35
count = 0


def perimeter(c, l):
    if c <= l:
        if 2 * (c + l) == 24:
            return True
    return False


for c in range(1, 12):
    for l in range(1, 12):
        if perimeter(c, l):
            count += 1


print(count)
