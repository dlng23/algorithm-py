class Node:
    def __init__(self, value, level):
        self.value = value
        self.level = level
    
import sys
K = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

result = []
def tree(level, arr):
    mid = len(arr) // 2
    result.append(Node(arr[mid], level))
    if len(arr) == 1:
        return
    tree(level+1, arr[:mid])
    tree(level+1, arr[mid+1:])

tree(0, num)

for i in range(K):
    for node in result:
        if node.level == i:
            print(node.value, end=' ')
    print()