n = 9
m = []
for i in range(n + 1):
    m.append([])
    for j in range(n + 1):
        m[i].append(0)
m[0][0] = 9
m[1][1] = 9

for i in range(n + 1):
    for j in range(n + 1):
        print m[i][j],
    print ''
