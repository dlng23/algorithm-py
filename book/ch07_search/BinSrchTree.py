# 코드 7.5: 이진 탐색 트리를 위한 노드 클래스
class BSTNode:                      # 이진 탐색 트리를 위한 노드 클래스               
    def __init__ (self, key, value):# 생성자: 키와 값을 받음
        self.key = key      # 키(key)
        self.value = value  # 값(value): 키를 제외한 데이터 부분
        self.left = None    # 왼쪽 자식에 대한 링크
        self.right = None   # 오른쪽 자식에 대한 링크


# 코드 7.6: 이진 탐색 트리의 탐색 연산(순환 구조)
def search_bst(n, key):
    if n == None:
        return None
    elif key == n.key:
        return n
    elif key < n.key:
        return search_bst(n.left, key)
    else:
        return search_bst(n.right, key)
    

# 코드 7.7: 이진 탐색 트리의 값을 이용한 탐색(전위 순회)
def search_value_bst(n, value):
    if n == None: return None
    elif value == n.value:
        return n
    res = search_value_bst(n.left, value)
    if res is not None:
        return res
    else:
        return search_value_bst(n.right, value)
    

# 코드 7.8: 이진 탐색 트리의 삽입 연산
def insert_bst(root, node): 
    if root == None:            # 공백 노드에 도달하면, 이 위치에 삽입
        return node             # node를 반환(이 노드가 현재 root 위치에 감)
    
    if node.key == root.key:    # 동일한 키는 허용하지 않음
        return root             # root를 반환(root는 변화 없음)
    
    # root의 서브 트리에 node 삽입
    if node.key < root.key:
        root.left = insert_bst(root.left, node)
    
    else:
        root.right = insert_bst(root.right, node)
    
    return root     # root를 반환(root는 변화 없음)


# 코드 7.9: 이진 탐색 트리의 삭제 연산
def delete_bst(root, key):
    if root == None:    # 공백 트리
        return root
    
    if key < root.key:
        root.left = delete_bst(root.left, key)
    elif key > root.key:
        root.right = delete_bst(root.right, key)

    # key가 루트의 키와 같으면 root를 삭제
    else:
        # case1(단말 노드) 또는 case2(오른쪽 자식만 있는 경우)
        if root.left == None:
            return root.right
        
        # case2(왼쪽 자식만 있는 경우)
        if root.right == None:
            return root.left
        
        # case3(두 자식이 모두 있는 경우):
        succ = root.right
        while succ.left != None:
            succ = succ.left

        root.key = succ.key
        root.value = succ.value
        root.right = delete_bst(root.right, succ.key)

    return root


# 코드 7.10: 이진 탐색 트리의 테스트 프로그램
def print_node(msg, n):
    print(msg, n if n != None else "탐색 실패")

def print_tree(msg, r):
    print(msg, end='')
    preorder(r)
    print()

data = [(6, "여섯"), (8, "여덟"), (2, "둘"), (4, "넷"), (7, "일곱"), 
        (5, "다섯"), (1, "하나"), (9, "아홉"), (3, "셋"), (0, "영")]

root = None                         # 루트 노드 초기화
for i in range(0, len(data)):       # 노드 순서대로 추가하기
    root = insert_bst(root, BSTNode(data[i][0], data[i][1]))

print_tree("최초: ", root)          # 최초의 트리 출력

n = search_bst(root, 3);    print_node("srch 3: ", n)
n = search_bst(root, 8);    print_node("srch 8: ", n)
n = search_bst(root, 0);    print_node("srch 0: ", n)
n = search_bst(root, 10);    print_node("srch 10: ", n)
n = search_value_bst(root, "둘");    print_node("srch 둘: ", n)
n = search_value_bst(root, "열");    print_node("srch 열: ", n)

root = delete_bst(root, 7);     print_tree("del 7: ", root)
root = delete_bst(root, 8);     print_tree("del 8: ", root)
root = delete_bst(root, 2);     print_tree("del 2: ", root)
root = delete_bst(root, 6);     print_tree("del 6: ", root)