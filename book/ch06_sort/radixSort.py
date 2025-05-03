# 코드 6.6: 기수 정렬 알고리즘
from collections import deque   # collections 모듈의 deque을 사용

def radix_sort(A):
    queues = []
    for i in range(BUCKETS):
        queues.append(deque())

    n = len(A)
    factor = 1                  # 가장 낮은 자리부터 시작
    for d in range(DIGITS):     # 각 자릿수에 대해 처리
        for i in range(n):      # 모든 항목을 따라 큐에 삽입
            queues[(A[i]//factor) % BUCKETS].append(A[i])
        
        i = 0
        for b in range(BUCKETS):
            while queues[b]:
                A[i] = queues[b].popleft()
                i += 1
        factor += BUCKETS       # 그다음 자릿수로 간다.
        print("step", d+1, A)   # 처리과정 출력용 문장

# 코드 6.7: 기수 정렬 테스트 프로그램
import random       # 난수 발생을 위해 random 모듈 포함 
BUCKETS = 10        # 10진법 사용
DIGITS = 4          # 최대 4자릿수 숫자를 정렬함함

# 리스트 내포(list comprehension)로 난수 10개로 이루어진 리스트 생성
data = [random.randint(1, 9999) for _ in range(10)]
radix_sort(data)
print("Radix:", data)