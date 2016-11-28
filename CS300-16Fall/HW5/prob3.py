inf = float('inf')


def findCycle(R):
    n = len(R)
    for i in range(n):
        if bellford(i, R):
            return
    print "No cycle"


def bellford(source, R):
    n = len(R)
    d = []
    p = []
    for i in range(n):
        d.append(inf)
        p.append(None)
    d[source] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[j] > d[i] + R[i][j]:
                    d[j] = d[i] + R[i][j]
                    p[j] = i

    cyc = -1
    for i in range(n):
        for j in range(n):
            if d[j] > d[i] + R[i][j]:
                cyc = j

    if cyc == -1:
        return False
    else:
        ini = cyc
        path = []
        for i in range(n):
            path.append(cyc)
            cyc = p[cyc]
            if cyc == ini:
                break
        for i in reversed(range(len(path))):
            print path[i],
        return True

G = [[inf, inf, inf, inf],
     [2, inf, inf, -2],
     [2, -2, inf, inf],
     [inf, inf, 2, inf]]

findCycle(G)
