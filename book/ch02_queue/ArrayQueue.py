class ArrayQueue:
    def __init__(self, capacity=10):    # 생성자 정의
        self.capacity = capacity    # 용량(고정)
        self.array = [None] * capacity  # 요소들을 저장할 배열
        self.front = 0  # 전단 인덱스
        self.rear = 0   # 후단 인덱스

    def isEmpty(self):
        return self.front == self.rear
    
    def isFull(self):
        return self.front == (self.rear + 1) % self.capacity
    
    def enqueue(self, item):    # 삽입 연산
        if not self.isFull():   # 포화 상태가 아닌 경우
            self.rear = (self.rear + 1) % self.capacity
            self.array[self.rear] = item
        else: pass 

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

''' 원형 큐: 테스트 프로그램
import random
q = ArrayQueue(8)

q.display("초기 상태")
while not q.isFull():
    q.enqueue(random.randint(0,100))
q.display("포화 상태")

print("삭제 순서: ", end='')
while not q.isEmpty():
    print(q.dequeue(), end=' ')
print()
'''