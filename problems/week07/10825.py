import sys

n = int(sys.stdin.readline())
data = []

for _ in range(n):
    name, x, y, z = sys.stdin.readline().split()
    data.append((name, int(x), int(y), int(z)))

sorted_data = sorted(data, key = lambda p: (-p[1], p[2], -p[3], p[0]))

for e in sorted_data:
    print(e[0])