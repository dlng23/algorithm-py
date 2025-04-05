# 영어 대문자에 대한 모스 코드 표
table=[('A','.-'), ('B','-...'), ('C','-.-.'), ('D','-..'),
       ('E','.'),('F','..-.'),('G','--.'),('H','....'),
       ('I','..'),('J','.---'),('K','-.-'),('L','.-..'),
       ('M','--'),('N','-.'),('O','---'),('P','.--.'),
       ('Q','--.-'),('R','.-.'),('S','...'),('T','-'),
       ('U','..-'),('V','...-'),('W','.--'),('X','-..-'),
       ('Y','-.--'),('Z','--..')]

# 모스 코드 인코딩 함수
def encode(ch):
    idx = ord(ch)-ord('A')  # 리스트에서 해당 문자의 인덱스
    return table[idx][1]    # 해당 문자의 모스 부호 반환

# 단순한 방법의 모스 코드 디코딩 함수
def decode_simple(morse):
    for tp in table:        # 모스 코드 표의 모든 문자에 대해
        if morse == tp[1]:  # 찾는 코드와 같으면
            return tp[0]    # 그 코드의 문자를 반환
        
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from book.ch04_tree.BinaryTree import BTNode
# 모스 코드 디코딩을 위한 결정 트리 만들기
def make_morse_tree():
    root = BTNode(None, None, None)
    for tp in table:        # tp: 모스 코드 표의 각 항목
        code = tp[1]        # tp[1]: 모스 코드
        node = root         # 루트부터 탐색
        for c in code:
            if c == '.':    # 점(.)이면 왼쪽으로 이동
                if node.left == None:
                    node.left = BTNode(None, None, None)
                node = node.left
            elif c == '-':  # 선(-)이면 오른쪽으로 이동
                if node.right == None:
                    node.right = BTNode(None, None, None)
                node = node.right

        node.data = tp[0]   # 최종 노드에 문자(tp[0]) 부여
    return root

# 결정 트리를 이용한 디코딩 함수
def decode(root, code):
    node = root                             # 루트 노드에서 시작
    for c in code:                          # 각 부호에 대해
        if c == '.' : node = node.left      # 점(.): 왼쪽으로 이동
        elif c == '-' : node = node.right   # 선(-): 오른쪽으로 이동
    return node.data                        # 문자 반환

# 인코딩과 디코딩 테스트 프로그램
morseCodeTree = make_morse_tree()
str = input("입력 문장 : ")
mlist = []
for ch in str:
    code = encode(ch)
    mlist.append(code)
print("Morse Code: ", mlist)
print("Decoding: ", end='')
for code in mlist:
    ch = decode(morseCodeTree, code)
    print(ch, end='')
print()