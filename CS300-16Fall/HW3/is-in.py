inf = float('inf')

def is_in(Y, i, j, k):
    if Y[i][j] < k:
        if i + 1 < len(Y):
            return is_in(Y, i + 1, j, k)
        else:
            return False
    elif Y[i][j] > k:
        if j - 1 >= 0:
            return is_in(Y, i, j - 1, k)
        else:
            return False
    else:
        return True

Y = [[2, 3, 4, 5], [8, 9, 12, inf], [14, 16, inf, inf], [inf, inf, inf, inf]]
for i in range(17):
    print is_in(Y, 0, len(Y[0]) - 1, i)
