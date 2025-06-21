# 코드 9.2: 0-1 배낭 채우기(억지 기법)
def Knapsack01_BF(wgt, val, W):
    n = len(wgt)        # 전체 물건의 수
    bestVal = 0         # 배낭의 최대 가치

    for i in range(2**n):
        s = [0]*n
        for d in range(n):
            s[d] = i%2
            i = i//2

        sumVal = 0
        sumWgt = 0
        for d in range(n):
            if s[d] == 1:
                sumWgt += wgt[d]
                sumVal += val[d]
            
        if sumWgt <= W:
            if sumVal > bestVal:
                bestVal = sumVal

    return bestVal      # 최대 가치 반환