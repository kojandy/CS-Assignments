import copy

G = [[0, 2, 1, 0, 0],
     [0, 0, 2, 0, 3],
     [0, 0, 0, 5, 7],
     [0, 0, 0, 0, 2],
     [0, 0, 0, 0, 0]]


def find(G, s):
    path = []
    for i in range(0, len(G)):
        path.append([])
        for j in range(0, len(s) + 1):
            path[i].append(None)
    path[0][0] = [0]
    for k in range(1, len(s) + 1):
        for i in range(0, len(G)):
            if path[i][k - 1] != None:
                for j in range(0, len(G)):
                    if G[i][j] == s[k - 1]:
                        path[j][k] = copy.copy(path[i][k - 1])
                        path[j][k].append(j)
    for i in range(len(G)):
        if path[i][len(s)] != None:
            print path[i][len(s)]
            return
    print "No-Such-Path"
    return

find(G, (2, 2, 5, 2))
