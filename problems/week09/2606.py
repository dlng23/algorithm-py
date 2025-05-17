n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(x):
    count = 0
    visited[x] = True
    for i in graph[x]:
        if not visited[i]:
            count += 1 + dfs(i)
    return count        

num = dfs(1)

print(num)