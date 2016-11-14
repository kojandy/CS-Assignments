G = [[1, 3],
     [0, 2, 3],
     [1, 4, 5],
     [0, 1, 4],
     [2, 3],
     [2]]


def color(G):
    A = [0 for x in range(len(G))]
    for i in range(len(G)):
        used = [False for x in range(len(G) + 2)]
        used[0] = True
        for j in G[i]:
            used[A[j]] = True
        for j in range(len(G) + 2):
            if not used[j]:
                A[i] = j
                break

    print A

color(G)
