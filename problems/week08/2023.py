import math

N = int(input())

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def dfs(num, depth):
    if depth == N:
        print(num)
        return
    for i in range(1, 10):
        new_num = num * 10 + i
        if is_prime(new_num):
            dfs(new_num, depth + 1)

dfs(2, 1)
dfs(3, 1)
dfs(5, 1)
dfs(7, 1)