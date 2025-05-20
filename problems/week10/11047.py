n, k = map(int, input().split())

m = []
for _ in range(n):
    m.append(int(input()))

count = 0
while k!=0:
    c = k // m[n-1]
    k = k % m[n-1]
    n = n-1
    count += c

print (count)