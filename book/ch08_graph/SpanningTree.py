# 코드 8.5: DFS를 이용한 신장트리(인접행렬 방식)
def ST_DFS(vtx, adj, s, visited):
    visited[s] = True
    for v in range(len(vtx)):
        if adj[s][v] != 0:
            if visited[v] == False:
                print("(", vtx[s], vtx[v], ")", end=' ')
                ST_DFS(vtx, adj, v, visited)