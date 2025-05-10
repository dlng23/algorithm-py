# 코드 7.1: 순차 탐색 알고리즘
def sequential_search(A, key, low, high):
    for i in range(low, high+1):    # i: low, low+1, ... high
        if A[i] == key:             # 탐색 성공하면
            return i                # 인덱스 반환
    return -1                       # 탐색에 실패하면 -1 반환


# 코드 7.2: 교환하기 전략이 추가된 순차 탐색 알고리즘
def sequential_search_transpose(A, key, low, high):
    for i in range(low, high+1):
        if A[i] == key:
            if i > low:             # 맨 처음 요소가 아니면
                A[i], A[i-1] = A[i-1], A[i] # 교환하기(transpose)
                i = i-1             # 한 칸 앞으로 왔음
            return i                # 탐색에 성공하면 키 값의 인덱스 반환
    return -1                       # 탐색에 실패하면 -1 반환


# 코드 7.3: 이진 탐색 알고리즘(순환 구조)
def binary_search(A, key, low, high):
    if (low <= high):               # 항목들이 남아 있으면(종료 조건)
        middle = (low + high)//2    # middle 계산
        if key == A[middle]:        # 탐색 성공
            return middle           # 중앙 레코드의 인덱스 반환
        elif (key < A[middle]):     # 왼쪽 부분리스트 탐색 -> 순환호출
            return binary_search(A, key, low, middle-1)
        else:                       # 오른쪽 부분리스트 탐색 -> 순환호출
            return binary_search(A, key, middle+1, high)
    return -1                       # 탐색 실패 -1 반환


# 코드 7.4: 이진 탐색 알고리즘(반복 구조)
def binary_search_iter(A, key, low, high):
    while (low <= high):            # 항목들이 남아 있으면(종료 조건)
        middle = (low + high)//2    # middle 계산
        if key == A[middle]:        # 탐색 성공
            return middle
        elif (key > A[middle]):     # key가 middle의 값보다 크면
            low = middle + 1        # middle+1 ~ high 사이 검색
        else:                       # key가 middle의 값보다 작으면
            high = middle - 1       # low ~ middle-1 사이 검색
    return -1                       # 탐색 실패 -1 반환


# 보간 탐색의 경우 middle 값을 아래와 같이 수정
# middle = int(low + (high-low) * (key-A[low]) / (A[high]-A[low]))