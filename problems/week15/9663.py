def isSafe(board, x, y):
    # N = len(board)

    # for i in range(y):
    #     if board[i][x] == 1:
    #         return False
    # for i, j in zip(range(y-1, -1, -1), range(x-1, -1, -1)):
    #     if board[i][j] == 1:
    #         return False
    # for i, j in zip(range(y-1, -1, -1), range(x+1, N)):
    #     if board[i][j] == 1:
    #         return False
    if col[x] or d1[y + x] or d2[y - x + N - 1]:
        return False
    return True

count = [0]
def solve_N_Queen(board, y):

    # N = len(board)
    if y == N:
        count[0] += 1
        return
    
    for x in range(N):
        if isSafe(board, x, y):
            board[y][x] = 1
            col[x] = True
            d1[y + x] = True
            d2[y - x + N - 1] = True

            solve_N_Queen(board, y+1)

            board[y][x] = 0
            col[x] = False
            d1[y + x] = False
            d2[y - x + N - 1] = False


N = int(input())

board = [[0 for i in range(N)] for j in range(N)]

col = [False] * N           
d1 = [False] * (2*N - 1)  
d2 = [False] * (2*N - 1)

solve_N_Queen(board, 0)
print(count[0])