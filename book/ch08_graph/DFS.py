# 코드 8.1: 깊이 우선 탐색(인접행렬 방식)
def DFS(vtx, adj, s, visited):
    print(vtx[s], end=' ')
    visited[s] = True

    for v in range(len(vtx)):
        if adj[s][v] != 0:
            if visited[v] == False:
                DFS(vtx, adj, v, visited)
