import sys

n = int(sys.stdin.readline())
data = []

for _ in range(n):
    age, name = sys.stdin.readline().split()
    data.append((int(age), name))

sorted_data = sorted(data, key = lambda p: p[0])

for e in sorted_data:
    print(e[0], e[1])