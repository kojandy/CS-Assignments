inf = float('inf')

def extract_min(Y):
    _min = Y[0][0]
    Y[0][0] = inf
    corr_young(Y, 0, 0)
    return _min

def corr_young(Y, i, j):
    right = inf
    down = inf
    if j + 1 < len(Y[i]):
        right = Y[i][j+1]
    if i + 1 < len(Y):
        down = Y[i + 1][j]

    if right < Y[i][j] or down < Y[i][j]:
        if down < right:
            Y[i][j], Y[i + 1][j] = Y[i + 1][j], Y[i][j]
            corr_young(Y, i + 1, j)
        else:
            Y[i][j], Y[i][j + 1] = Y[i][j + 1], Y[i][j]
            corr_young(Y, i, j + 1)

Y = [[2, 3, 4, 5], [8, 9, 12, inf], [14, 16, inf, inf], [inf, inf, inf, inf]]
for i in range(9):
    print extract_min(Y)
