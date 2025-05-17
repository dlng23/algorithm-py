# 코드 8.3: 너비 우선 탐색(인접 리스트 방식)
from queue import Queue
def BFS_AL(vtx, aList, s):
    n = len(vtx)
    visited = [False]*n
    Q = Queue()
    Q.put(s)
    visited[s] = True
    while not Q.empty():
        s = Q.get()
        print(vtx[s], end=' ')
        for v in aList[s]:
            if visited[v]==False:
                Q.put(v)
                visited[v] = True