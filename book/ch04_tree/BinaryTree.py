class BTNode:
    def __init__ (self, elem, left=None, right=None):
        self.data = elem
        self.left = left    # 왼쪽 자식을 위한 링크
        self.right = right  # 오른쪽 자식을 위한 링크

    def isLeaf(self):
        return self.left is None and self.right is None
    

# 전위순회 함수
def preorder(n):    
    if n is not None:
        print(n.data, end=' ')
        preorder(n.left)    # 왼쪽 서브 트리 처리
        preorder(n.right)   # 오른쪽 서브 트리 처리


# 중위순회 함수  
def inorder(n):    
    if n is not None:
        inorder(n.left)     # 왼쪽 서브 트리 처리
        print(n.data, end=' ')    
        inorder(n.right)   # 오른쪽 서브 트리 처리


# 후위순회 함수
def postorder(n):
    if n is not None:
        postorder(n.left)
        postorder(n.right)
        print(n.data, end=' ')


import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from book.ch02_queue.ArrayQueue import ArrayQueue
# 이진 트리의 레벨 순회
def levelorder(root) :
    queue = ArrayQueue()    # 큐 객체 초기화
    queue.enqueue(root)     # 최초에 루트 노드만 들어있음.
    while not queue.isEmpty():  # 큐가 공백 상태가 아닌 동안,
        n = queue.dequeue()
        if n is not None:
            print(n.data, end=' ')
            queue.enqueue(n.left)
            queue.enqueue(n.right)


# 이진 트리의 노드 수 구하기
def count_node(n):
    if n is None:   # n이 None이면 공백 트리 --> 0을 반환
        return 0
    else:           # 좌우 서브 트리의 노드 수의 합 + 1 (순환이용)
        return count_node(n.left) + count_node(n.right) + 1
    

# 이진 트리의 높이 구하기
def calc_height(n):
    if n is None:   # 공백 트리 --> 0을 반환환
        return 0
    hLeft = calc_height(n.left)     # hLeft <- L의 높이
    hRight = calc_height(n.right)   # hRight <- R의 높이
    if (hLeft > hRight):    # 더 큰 값에 1을 더해 반환
        return hLeft + 1
    else: return hRight + 1


'''
# 이진 트리 연산의 테스트 프로그램
d = BTNode('D', None, None)
e = BTNode('E', None, None)
b = BTNode('B', d, e)
f = BTNode('F', None, None)
c = BTNode('C', f, None)
root = BTNode('A', b, c)

print('\n In-Order : ', end=' '); inorder(root)
print('\n Pre-Order : ', end=' '); preorder(root)
print('\n Post-Order : ', end=' '); postorder(root)
print('\n Level-Order : ', end=' '); levelorder(root)
print()

print(" 노드의 개수 = %d개" % count_node(root))
print(" 트리의 높이 = %d" % calc_height(root))
'''