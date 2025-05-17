# 런타임 에러
t = int(input())
answers = []

for _ in range(t):
    h, w = map(int, input().split())
    board = [list(input()) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]

    def dfs(r, c):
        visited[r][c] = True
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            r2 = r + dr
            c2 = c + dc
            if 0 <= r2 < h and 0 <= c2 < w:
                if board[r2][c2] == '#' and not visited[r2][c2]:
                    dfs(r2, c2)

    count = 0
    for r in range(h):
        for c in range(w):
            if board[r][c] == '#' and not visited[r][c]:
                dfs(r, c)
                count += 1

    answers.append(str(count))

for ans in answers:
    print(ans)


# <잘못 생각한 방식> -> 사방을 다 고려해야 함 
# t = int(input())

# for _ in range(t):
#     h, w = map(int, input().split())
#     a = [list(input()) for _ in range(h)]

#     count = 0
#     for i in range(h):
#         for j in range(w):
#             if a[i][j] == '#':
#                 if (i == 0 or a[i-1][j] != '#') and (j == 0 or a[i][j-1] != '#'):
#                     count += 1

#     print(count)
