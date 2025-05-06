import sys

N = int(sys.stdin.readline())

ans = []

for _ in range(N):
    data = list(map(int, sys.stdin.readline().split()))
    data.sort(reverse=True)  
    ans.append(data[2])  
    
for e in ans:
    print(e)