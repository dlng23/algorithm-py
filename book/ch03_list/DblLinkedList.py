class DNode:
    def __init__(self, elem, prev=None, next=None):
        self.data = elem    # 노드의 데이터 필드(요소)
        self.next = next    # 다음 노드를 위한 링크
        self.prev = prev    # 이전 노드를 위한 링크(추가됨)

    def append(self, node): # self 다음에 node를 넣는 연산
        if node is not None:    # node가 None이 아니면
            node.next = self.next   # 1.
            node.prev = self    # 2.
            if node.next is not None:   # 3. self의 다음 노드가 있으면
                node.next.prev = node   # 그 노드의 이전 노드는 node
            self.next = node    # 4.
    
    def popNext(self):  # self 다음 노드 삭제 연산
        node = self.next    # 삭제할 노드
        if node is not None:    # next가 None이 아니면
            self.next = node.next   # 1.
            if self.next is not None:   # 2. 다음 노드가 있으면
                self.next.prev = self   # 그 노드의 이전 노드는 self
        return node # 다음 노드를 반환
    
class DblinkedList: # 이중 연결 리스트 클래스
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
            ptr = ptr.next
        return ptr  # 최종 노드를 반환
    
    def getEntry(self, pos):
        node = self.getNode(pos)    # pos번째 노드를 구함
        if node == None: return None    # 해당 노드가 없는 경우
        else: return node.data  # 있는 경우 데이터 필드 반환

    def size(self):
        ptr = self.head
        count = 0
        while ptr is not None:  # ptr이 None이 아닌 동안
            ptr = ptr.next  # 링크를 따라 ptr 이동
            count += 1  # 이동할 때마다 count 증가
        return count    # count 반환
    
    def display(self, msg='DblLinkedList:'):
        print(msg, end='')
        ptr = self.head
        while ptr is not None:
            print(ptr.data, end='<=>')
            ptr = ptr.next
        print('None')

    def replace(self, pos, e):
        node = self.getNode(pos)
        if node == None: return None
        else: node.data = e

    def insert(self, pos, e):
        node = DNode(e)
        before = self.getNode(pos-1)    # 삽입할 위치 이전 노드 탐색
        if before == None:  # 머리 노드로 삽입하는 경우
            node.next = self.head
            if node.next is not None:
                node.next.prev = node
            self.head = node
        else: before.append(node)   # 아닌 경우: before 다음에 추가

    def delete(self, pos):
        before = self.getNode(pos-1)
        if before == None:  # 머리 노드 삭제 경우
            before = self.head
            if self.head is not None:
                self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            return before
        else: before.popNext()  # before의 다음 노드 삭제
        

# 이중 연결 리스트(DblLinkedList)
s = DblinkedList()
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