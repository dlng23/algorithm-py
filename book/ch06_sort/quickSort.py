# 코드 6.4: 퀵 정렬 알고리즘
def quick_sort(A, left, right):
    if left<right:      # 정렬 범위가 2개 이상인 경우
        q = partition(A, left, right)
        quick_sort(A, left, q-1)
        quick_sort(A, q+1, right)

# 코드 6.5: 분할 알고리즘
def partition(A, left, right):
    pivot = A[left]
    low = left + 1
    high = right

    while (low < high):     # low와 high가 역전되지 않는 한 반복
        while low <= right and A[low] <= pivot:
            low += 1        # A[low]<=pivot이면 low를 오른쪽으로 진행

        while high >= left and A[high] > pivot:
            high -= 1       # A[high]>pivot이면 high를 왼쪽으로 진행
        
        if low < high:      # 역전이 아니면 두 레코드 교환
            A[low], A[high] = A[high], A[low]

    A[left], A[high] = A[high], A[left]
    return high