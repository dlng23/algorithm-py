tc = int(input())

ans = []
for _ in range (tc):
    n, m = map(int, input().split())
    for _ in range(m):
        input()
    ans.append(n-1)

for i in ans:
    print(i)