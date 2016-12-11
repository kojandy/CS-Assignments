# 2016 Falll CS300 Programming Assignment #2
# Due: 2016.12.12 11:59 PM
# TA in charge of PA2: Sehyun Joo (shjoodm@kaist.ac.kr)

def find_s_path(departure,destination):
    map_initialize()

    inf = float('inf')
    n = len(cities)
    dep = cities.index(departure)
    des = cities.index(destination)

    d = [inf for i in range(n)]
    d[dep] = 0
    q = {i for i in range(n)}
    path = [[] for i in range(n)]
    while q:
        u = -1
        min_val = inf
        for i in q:
            if d[i] < min_val:
                u = i
                min_val = d[i]
        q.remove(u)
        if u == des:
            return (d[des], path[des])
        for v in range(n):
            if distance[u][v] != -1 and d[v] > d[u] + distance[u][v]:
                d[v] = d[u] + distance[u][v]
                path[v] = path[u][:]
                path[v].append(cities[v])

    return -1

#============================================================
# WARNING
# DO NOT MODIFY THE CODE BELOW
#============================================================
def map_initialize():
    global cities, distance
    cities = ['cheorwon','yeoncheon','sokcho','yangyang','gimpo','seoul','incheon','gangneung','yongin','wonju','taebaek','yeongju','uljin','goesan','andong','gongju','daejeon','pohang','jeonju','daegu','cheongdo','ulsan','gwangju','gurye','gimhae','hampyeong','gwangyang','busan','sinan','jindo','goheung','yeosu']
    distance = [[-1,22,110,-1,-1,71,-1,-1,105,110,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                [22,-1,-1,-1,69,60,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                [110,-1,-1,16,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                [-1,-1,16,-1,-1,-1,-1,45,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                [-1,69,-1,-1,-1,-1,18,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                [71,60,-1,-1,24,-1,28,-1,41,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                [-1,-1,-1,-1,18,28,-1,-1,50,-1,-1,-1,-1,-1,-1,123,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                [-1,-1,-1,45,-1,-1,-1,-1,-1,-1,67,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                [105,-1,-1,-1,-1,41,50,-1,-1,71,-1,-1,-1,75,-1,88,104,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                [110,-1,-1,-1,-1,-1,-1,-1,71,-1,103,93,-1,60,-1,-1,125,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                [-1,-1,-1,-1,-1,-1,-1,67,-1,103,-1,53,42,-1,70,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                [-1,-1,-1,-1,-1,-1,-1,-1,-1,93,53,-1,77,76,29,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,42,77,-1,-1,78,-1,-1,113,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                [-1,-1,-1,-1,-1,-1,-1,-1,75,60,-1,76,-1,-1,91,-1,65,-1,-1,130,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,70,29,78,91,-1,-1,125,84,-1,80,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                [-1,-1,-1,-1,-1,-1,123,-1,88,-1,-1,-1,-1,-1,-1,-1,26,-1,71,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                [-1,-1,-1,-1,-1,-1,-1,-1,104,125,-1,-1,-1,65,125,26,-1,-1,64,125,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,113,-1,84,-1,-1,-1,-1,70,70,55,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,71,64,-1,-1,131,149,-1,81,77,-1,-1,-1,-1,-1,-1,-1,-1],
                [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,130,80,-1,125,70,131,-1,29,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,70,149,29,-1,55,-1,128,49,-1,-1,-1,-1,-1,-1,-1],
                [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,55,-1,-1,55,-1,-1,-1,52,-1,-1,47,-1,-1,-1,-1],
                [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,81,-1,-1,-1,-1,56,-1,33,-1,-1,-1,-1,75,-1],
                [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,77,-1,128,-1,56,-1,134,-1,38,-1,-1,-1,-1,-1],
                [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,49,52,-1,134,-1,-1,119,18,-1,-1,-1,-1],
                [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,33,-1,-1,-1,-1,-1,-1,70,-1,-1],
                [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,38,119,-1,-1,-1,-1,-1,62,21],
                [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,47,-1,-1,18,-1,-1,-1,-1,-1,-1,-1],
                [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,28,-1,-1],
                [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,70,-1,-1,28,-1,98,-1],
                [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,75,-1,-1,-1,62,-1,-1,98,-1,-1],
                [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,21,-1,-1,-1,-1,-1]]
    return

if __name__ == '__main__':
    find_s_path('seoul','busan')

