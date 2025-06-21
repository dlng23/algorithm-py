def ways(n):
    sw = [0] * (n + 3)
    sw[0] = 1
    for i in range(1, n + 1):
        sw[i] = sw[i - 1] + sw[i - 2] + sw[i - 3]
    return sw[n]

tc = int(input())
ans=[]
for _ in range(tc):
    n = int(input())
    ans.append(ways(n))

for i in ans:
    print(i)  