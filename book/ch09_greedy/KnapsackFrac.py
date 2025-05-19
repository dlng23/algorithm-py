# 코드 9.3: 분할 가능한 배낭 채우기(탐욕적 기법)
def KnapSackFrac(wgt, val, W):
    bestVal = 0         # 최대가치
    for i in range(len(wgt)):   # 단가가 높은 물건부터 처리
        if W <= 0:      # 용량이 다 찼으면 채우기 종료
            break
        if W >= wgt[i]:
            W -= wgt[i]
            bestVal += val[i]
        else:
            fraction = W / wgt[i]
            bestVal += val[i] * fraction
            break

    return bestVal  # 최대 가치 반환

# 테스트 프로그램
weight = [12, 10, 8]    # (정렬됨)
value = [120, 80, 60]   # (정렬됨)
W = 18          # 배낭의 제한 용량
print("Fractional Knapsack(18):", KnapSackFrac(weight, value, W))