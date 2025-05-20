n = int(input())

p = list(map(int, input().split()))

sorted_p = sorted(p)

min = 0
for i in range(n):
    min += sorted_p[i]*(n-i)

print(min)