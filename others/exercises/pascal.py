# Triangulo de Pascal
n = 9
m = []
for i in range(n + 1):
    m.append([])
    for j in range(n + 1):
        m[i].append(1)
m[0][0] = 1
m[1][1] = 1

for i in range(n + 1):
    for j in range(i + 1):
        if j == 0:
            m[i][j] = m[i - 1][j]
        else:
            if j == i + 1:
                m[i][j] = m[i - 1][j - 1]
            else:
                m[i][j] = m[i - 1][j] + m[i - 1][j - 1]

for i in range(n + 1):
    for j in range(n + 1):
        print m[i][j],
    print ''
