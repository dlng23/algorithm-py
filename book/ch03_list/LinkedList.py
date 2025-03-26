class Node:
    def __init__ (self, elem, link=None):
        self.data = elem    # 데이터 멤버 생성 및 초기화
        self.link = link    # 링크 생성 및 초기화   

    def append (self, node):    # self 다음에 node를 넣는 연산
        if node is not None:
            node.link = self.link
            self.link = node
    
    def popNext (self): # self의 다음 노드를 삭제하는 연산
        next = self.link    # 현재 노드(self)의 다음 노드
        if next is not None:
            self.link = next.link
        return next # 다음 노드를 반환

class LinkedList:   # 단순 연결 리스트 클래스
    def __init__(self): # 생성자
        self.head = None    # head 선언 및 None으로 초기화

    def isEmpty(self):  # 공백 상태 검사
        return self.head == None    # head가 None이면 공백
    
    def isFull(self):   # 포화 상태 검사
        return False    # 연결된 구조에서는 포화 상태 없음

    def getNode(self, pos):
        if pos < 0 : return None    # 잘못된 위치 -> None
        ptr = self.head # 시작 위치 -> head
        for i in range(pos):
            if ptr == None:
                return None
            ptr = ptr.link
        return ptr  # 최종 노드를 반환
    
    def getEntry(self, pos):
        node = self.getNode(pos)    # pos번째 노드를 구함
        if node == None: return None    # 해당 노드가 없는 경우
        else: return node.data  # 있는 경우 데이터 필드 반환
    
    def insert(self, pos, e):
        node = Node(e, None)    # 삽입할 새로운 노드를 만듦
        before = self.getNode(pos-1)    # 삽입할 위치 이전 노드 탐색
        if before == None:
            node.link = self.head
            self.head = node
        else: before.append(node)   # 아닌 경우: before 뒤에 추가

    def delete(self, pos):
        before = self.getNode(pos-1)
        if before == None:  # 이전 노드가 없는 경우 (헤더 노드를 지우려는 경우)
            before = self.head  # 리스트가 비어 있는 경우 before = None이 되고 None 반환
            if self.head is not None:   # 리스트가 비어 있지는 않은 지 확인
                self.head = self.head.link  # 다음 노드가 head가 되도록 수정
            return before
        else: return before.popNext()   # before의 다음 노드 삭제
    
    def size(self):
        ptr = self.head
        count = 0
        while ptr is not None:  # ptr이 None이 아닌 동안
            ptr = ptr.link  # 링크를 따라 ptr 이동
            count += 1  # 이동할 때마다 count 증가
        return count    # count 반환
    
    def display(self, msg='LinkedList:'):
        print(msg, end='')
        ptr = self.head
        while ptr is not None:
            print(ptr.data, end='->')
            ptr = ptr.link
        print('None')

    def replace(self, pos, e):
        node = self.getNode(pos)
        if node == None: return None
        else: node.data = e


# 단순 연결 리스트(LinkedList)
s = LinkedList()
s.display('연결리스트(초기): ')
s.insert(0, 10)
s.insert(0, 20)
s.insert(1, 30)
s.insert(s.size(), 40)
s.insert(2, 50)
s.display("연결리스트(삽입x5): ")
s.replace(2, 90)
s.display("연결리스트(교체x1): ")
s.delete(2)
s.delete(3)
s.delete(0)
s.display("연결리스트(삭제x3): ")


print("\n")


# 파이썬의 리스트
l = []
print('파이썬list(초기):', l)
l.insert(0, 10)
l.insert(0, 20)
l.insert(1, 30)
l.insert(len(l), 40)
l.insert(2, 50)
print('파이썬list(삽입x5):', l)
l[2] = 90
print('파이썬list(교체x1):', l)
l.pop(2)
l.pop(3)
l.pop(0)
print('파이썬list(삭제x3):', l)