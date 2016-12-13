def topo_sort(G):
    indeg = [0 for i in range(len(G))]
    q = []
    sort = []

    for i in range(len(G)):
        for v in G[i]:
            indeg[v] += 1

    for i in range(len(indeg)):
        if indeg[i] == 0:
            q.append(i)

    while q:
        top = q.pop(0)
        sort.append(top)
        for v in G[top]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    return sort


G = [[4, 5, 11],
     [2, 4, 8],
     [5, 6, 9],
     [2, 6, 13],
     [7],
     [8, 12],
     [5],
     [],
     [7],
     [10, 11],
     [13],
     [],
     [9],
     []]
print(topo_sort(G))
