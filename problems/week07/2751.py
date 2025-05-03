import sys

n = int(sys.stdin.readline())
data = []

for _ in range(n):
    data.append(int(sys.stdin.readline()))

sorted_data = sorted(data)

for e in sorted_data:
    print(e)