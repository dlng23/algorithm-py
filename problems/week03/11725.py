import sys

n = int(sys.stdin.readline())
tree = {}       
parent = {}     

for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())

    if a not in tree:
        tree[a] = []
    if b not in tree:
        tree[b] = []

    tree[a].append(b)
    tree[b].append(a)

def find_p(node, p):
    parent[node] = p
    for child in tree[node]:
        if child not in parent:
            find_p(child, node)

find_p(1, 0)

for i in range(2, n + 1):
    print(parent[i])