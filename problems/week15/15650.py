N, M = map(int, input().split())

result = []

def backtrack(n):
    if len(result) == M:
        print(' '.join(map(str, result)))
        return
    
    for i in range(n, N+1):
        result.append(i)
        backtrack(i+1)
        result.pop()

backtrack(1)