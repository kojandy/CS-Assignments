Z = []


def go(x, y):
    if (x, y) not in Z:
        Z.append((x, y))
    if x < 10 and y < 10:
        go(x + 1, y + 1)
    if x > 1 and y < 10:
        go(x - 1, y + 1)

go(2, 4)
Z.sort()
print Z
