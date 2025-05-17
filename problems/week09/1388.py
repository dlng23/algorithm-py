n, m = map(int, input().split())

f = [list(input()) for _ in range(n)]
count = 0

for i in range(n):
    for j in range(m):
        if f[i][j] == '-':
            if j == 0 or f[i][j - 1] != '-':
                count += 1
        elif f[i][j] == '|':
            if i == 0 or f[i - 1][j] != '|':
                count += 1

print(count)