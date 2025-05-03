import sys

n = int(sys.stdin.readline())
data = []

for _ in range(n):
    x, y = sys.stdin.readline().split()
    data.append((int(x), int(y)))

sorted_data = sorted(data, key = lambda p: (p[1], p[0]))

for e in sorted_data:
    print(e[0], e[1])