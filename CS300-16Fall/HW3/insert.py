import random

inf = float('inf')

def insert(Y, a):
    m = len(Y)
    n = len(Y[0])
    Y[m - 1][n - 1] = a
    corr_young(Y, m - 1, n - 1)

def corr_young(Y, i, j):
    up = -inf
    left = -inf
    if i - 1 >= 0:
        up = Y[i - 1][j]
    if j - 1 >= 0:
        left = Y[i][j - 1]

    if Y[i][j] < up or Y[i][j] < left:
        if left < up:
            Y[i][j], Y[i - 1][j] = Y[i - 1][j], Y[i][j]
            corr_young(Y, i - 1, j)
        else:
            Y[i][j], Y[i][j - 1] = Y[i][j - 1], Y[i][j]
            corr_young(Y, i, j - 1)

Y = [[inf, inf, inf, inf], [inf, inf, inf, inf], [inf, inf, inf, inf], [inf, inf, inf, inf]]
for i in range(16):
    insert(Y, random.randrange(1, 51))
    print Y
