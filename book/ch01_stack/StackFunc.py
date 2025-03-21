capacity = 10   # 스택 용량: 예) 용량을 10으로 지정 
array = [None]*capacity # 요소 배열: [None, ..., None] (길이가 capacity)
top = -1    # 상단의 인덱스: 공백 상태(-1)로 초기화

def isEmpty() :
    if top == -1 : return True  # 공백이면 True 반환
    else : return False # 아니면 False 반환

def isFull() : return top == capacity # 비교 연산 결과를 바로 반환

def push(e): 
    # global top
    if not isFull(): # 포화 상태가 아닌 경우
        top += 1    # top 증가(global top 선언 필요)
        array[top] = e  # top 위치에 e 복사
    else:   # 포화 상태: overflow
        print("stack overflow")
        exit()

def pop(): 
    # global top
    if not isEmpty():   # 공백 상태가 아닌 경우
        top -= 1    # top 감소(global top 선언 필요)
        return array[top+1] # 이전 (top+1) 위치의 요소 반환
    else:   # 공백 상태: underflow 
        print("stack underflow")
        exit()

def peek():
    if not isEmpty():   # 공백 상태가 아닌 경우
        return array[top]
    else: pass  # underflow 예외는 처리하지 않았음

def size(): return top+1 # 현재 요소의 수는 top+1