from ArrayQueue_Ring import ArrayQueue_Ring

class CircularDeque(ArrayQueue_Ring):    # ArrayQueue_Ring: 부모 클래스 / CircularDeque: 자식 클래스
    def __init__(self, capacity=10):    # 생성자는 상속되지 않으므로 다시 구현해야 함
        super().__init__(capacity)  # 부모의 생성자를 호출하여 부모 클래스의 데이터 초기화

    def addRear(self, item): self.enqueue2(item)
    def deleteFront(self): return self.dequeue()
    def getFront(self): return self.peek()

    def addFront(self, item):
        if not self.isFull():   # 포화 상태가 아닐 경우
            self.array[self.front] = item   # front에 요소 삽입입
            self.front = (self.front-1+self.capacity) % self.capacity   # front를 반시계 방향으로 회전
        else: pass

    def deleteRear(self):
        if not self.isEmpty():  # 공백 상태가 아닐 경우
            item = self.array[self.rear]    # rear 요소 복사해둠
            self.rear = (self.rear-1+self.capacity) % self.capacity # rear를 반시계 방향으로 회전
            return item # 복사해둔 요소 반환
        else: pass

    def getRear(self):
        if not self.isEmpty():  # 공백 상태가 아닐 경우
            return self.array[self.rear]    # rear 요소 반환
        else: pass

''' 원형 덱의 테스트 프로그램
dq = CircularDeque()

for i in range(9):
    if i%2==0: dq.addRear(i)
    else: dq.addFront(i)
dq.display("홀수는 전단 짝수는 후단 삽입")

for i in range(2): dq.deleteFront()
for i in range(3): dq.deleteRear()
dq.display("전단 삭제 2번, 후단 삭제 3번")

for i in range(9, 14): dq.addFront(i)
dq.display("전단에 9~13 삽입")
'''