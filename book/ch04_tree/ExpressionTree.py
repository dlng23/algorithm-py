# 수식 트리 계산 함수
def evaluate(node):
    if node is None:        # 공백 트리이면 0 반환
        return 0
    elif node.isLeaf():     # 단말 노드이면 -> 피연산자
        return node.data    # 그 노드의 값(데이터) 반환
    else:                   # 루트나 가지노드라면 -> 연산자자
        op1 = evaluate(node.left)
        op2 = evaluate(node.right)
        if node.data == '+' : return op1 + op2
        elif node.data == '-' : return op1 - op2
        elif node.data == '*' : return op1 * op2
        elif node.data == '/' : return op1 / op2


import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from book.ch04_tree.BinaryTree import BTNode, preorder, inorder, postorder
# 후위표기 수식을 이용한 수식 트리 만들기
def buildTree(expr):
    if len(expr) == 0:
        return None
    
    token = expr.pop()
    if token in "+-*/":
        node = BTNode(token)
        node.right = buildTree(expr)
        node.left = buildTree(expr)
        return node
    else: 
        return BTNode(float(token))
    

# 수식 트리 테스트 프로그램
str = input("입력(후위표기): ")     # 후위표기식 입력
expr = str.split()                 # 토큰 리스트로 변환
print("토큰분리(expr): ", expr)
root = buildTree(expr)
print('\n 전위순회: ', end=''); preorder(root)
print('\n 중위순회: ', end=''); inorder(root)
print('\n 후위순회: ', end=''); postorder(root)
print('\n 계산 결과 : ', evaluate(root)) # 수식 트리 계산