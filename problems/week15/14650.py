N = int(input())

def sol(l, num):
    if l == N:
        if num % 3 == 0:
            return 1
        else: return 0

    count = 0
    for i in range(3):
        count += sol(l+1, num*10 + i)
    return count

result = 0
for i in [1, 2]:
    result += sol(1, i)

print(result)