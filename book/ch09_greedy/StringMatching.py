# 코드 9.1: 문자열 매칭(억지 기법)
def string_matching(T, P):      # T: 입력 문자열(텍스트), P: 탐색 패턴
    n = len(T)      # n: 텍스트의 길이
    m = len(P)      # m: 패턴의 길이

    for i in range(n-m+1):
        j = 0
        while j < m and P[j]==T[i+j]:
            j =j + 1
        if j == m:
            return i    # 매칭 성공
    return -1       # 매칭 실패