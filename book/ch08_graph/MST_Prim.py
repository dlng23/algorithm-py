# 코드 8.7: MST에 포함되지 않은 최소 dist의 정점 찾기
INF = 999
def getMinVertex(dist, selected):
    minv = 0
    mindist = INF
    for v in range(len(dist)):
        if selected[v]==False and dist[v]<mindist:
            mindist = dist[v]
            minv = v
        return minv
    

# 코드 8.8: 프림의 최소 신장 트리 알고리즘
def MSTPrim(vertex, adj):
    n = len(vertex)
    dist = [INF] * n
    dist[0] = 0
    selected = [False] * n

    for _ in range(n):
        u = getMinVertex(dist, selected)
        selected[u] = True
        print(vertex[u], end=' ')
        for v in range(n):
            if adj[u][v] != INF and not selected[v]:
                if adj[u][v]<dist[v]:
                    dist[v]=adj[u][v]

        print(': ', dist)  