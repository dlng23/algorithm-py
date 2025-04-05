class BTNode:
    def __init__ (self, elem, left=None, right=None):
        self.data = elem
        self.left = left    # 왼쪽 자식을 위한 링크
        self.right = right  # 오른쪽 자식을 위한 링크

def preorder(n):    
    if n and n.data != '.':
        print(n.data, end='')
        preorder(n.left)    # 왼쪽 서브 트리 처리
        preorder(n.right)   # 오른쪽 서브 트리 처리
 
def inorder(n):    
    if n and n.data != '.':
        inorder(n.left)     # 왼쪽 서브 트리 처리
        print(n.data, end='')    
        inorder(n.right)   # 오른쪽 서브 트리 처리


def postorder(n):
    if n and n.data != '.':
        postorder(n.left)
        postorder(n.right)
        print(n.data, end='')

import sys
N = int(sys.stdin.readline())
tree = {}

for i in range(N):
    p, l, r = list(sys.stdin.readline().split())
    
    if p not in tree:
        tree[p] = BTNode(p)
    
    if l != '.':
        if l not in tree:
            tree[l] = BTNode(l)
        tree[p].left = tree[l]
    else: tree[p].left = None

    if r != '.':
        if r not in tree:
            tree[r] = BTNode(r)
        tree[p].right = tree[r]
    else: tree[p].right = None

root = tree['A']
preorder(root)
print('')
inorder(root)
print('')
postorder(root)


'''
문제
이진 트리를 입력받아 전위 순회(preorder traversal), 중위 순회(inorder traversal), 후위 순회(postorder traversal)한 결과를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에는 이진 트리의 노드의 개수 N(1 ≤ N ≤ 26)이 주어진다. 둘째 줄부터 N개의 줄에 걸쳐 각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드가 주어진다. 노드의 이름은 A부터 차례대로 알파벳 대문자로 매겨지며, 항상 A가 루트 노드가 된다. 자식 노드가 없는 경우에는 .으로 표현한다.

출력
첫째 줄에 전위 순회, 둘째 줄에 중위 순회, 셋째 줄에 후위 순회한 결과를 출력한다. 각 줄에 N개의 알파벳을 공백 없이 출력하면 된다.
'''