class ArrayQueue_Ring:
    def __init__(self, capacity=10):    # 생성자 정의
        self.capacity = capacity    # 용량(고정)
        self.array = [None] * capacity  # 요소들을 저장할 배열
        self.front = 0  # 전단 인덱스
        self.rear = 0   # 후단 인덱스

    def isEmpty(self):
        return self.front == self.rear
    
    def isFull(self):
        return self.front == (self.rear + 1) % self.capacity
    
    def enqueue2(self, item):
        self.rear = (self.rear + 1) % self.capacity
        self.array[self.rear] = item
        if self.isEmpty():  # front==rear
            self.front = (self.front + 1) % self.capacity 

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            return self.array[self.front]
        else: pass
    
    def peek(self):
        if not self.isEmpty():
            return self.array[(self.front + 1) % self.capacity]
        else: pass

    def size(self):
        return (self.rear - self.front + self.capacity) % self.capacity
    
    def display(self, msg):
        print(msg, end='= [ ')
        for i in range(self.front+1, self.front+1+self.size()):
            print(self.array[i%self.capacity], end=' ')
        print("]")

''' 링 버퍼의 테스트 프로그램
q = ArrayQueue_Ring(8)

q.display("초기 상태")
for i in range(6):
    q.enqueue2(i)
q.display("삽입 0-5")

q.enqueue2(6); q.enqueue2(7)
q.display("삽입 6, 7")

q.enqueue2(8); q.enqueue2(9)
q.display("삽입 8, 9")

q.dequeue(); q.dequeue()
q.display("삭제 x2")
'''