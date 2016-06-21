# -*-coding:utf-8-*-
for i in range(100):
    print(i)

A = range(5 + 1)
B = range(5 + 1)
C = range(10 + 1)
j = 1
for i in range(1, 10 + 1, 2):
    C[i] = A[j]
    C[i + 1] = -B[j]
    j += 1
for i in range(1, 10 + 1):
    print(C[i])
