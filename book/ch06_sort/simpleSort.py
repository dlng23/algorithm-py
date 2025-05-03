# 코드 6.1: 선택 정렬 알고리즘(제자리 정렬 방식)
def selection_sort(A):
    n = len(A)  # 리스트의 크기
    for i in range(n-1): 
        least = i
        for j in range(i+1, n):
            if (A[j]<A[least]):
                least = j
        A[i], A[least] = A[least], A[i]    # A[i]와 A[least] 교환
        print("Step %2d = "%(i+1), A)   # 단계별 리스트 변화 출력


# 코드 6.2: 선택 정렬 테스트 프로그램
data = [6, 3, 7, 4, 9, 1, 5, 2, 8]
print("Original :", data)
selection_sort(data)
print("Selection :", data)