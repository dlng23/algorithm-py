n = int(input())
k = int(input())
cards = [input().strip() for _ in range(n)]

ans = set()

def dfs(c, u):
    if len(c) == k:
        ans.add(''.join(c))
        return

    for i in range(n):
        if i in u:
            continue
        dfs(c + [cards[i]], u + [i])

dfs([], [])
print(len(ans))
