def knapSack_dc(W, wt, val, n):
    if n == 0 or W == 0:
        return 0
        
    if (wt[n-1] > W):
        return knapSack_dc(W, wt, val, n-1)
    else:
        valWithout = knapSack_dc(W, wt, val, n-1)
        valWith = val[n-1] + knapSack_dc(W-wt[n-1], wt, val, n-1)
        return max(valWith, valWithout)
    
def kanpSack_dp(W, wt, val, n):
    A = [[0 for x in range(W + 1)] for x in range(n+1)]

    for i in range(1, n+1):
        for w in range(1, W+1):
            if wt[i-1] > w:
                A[i][w] = A[i-1][w]
            else:
                valWith = val[i-1] + A[i-1][w-wt[i-1]]
                valWithout = A[i-1][w]
                A[i][w] = max(valWith, valWithout)

    return A[n][W]

val = [60, 100, 190, 120, 200, 150]
wt = [2, 5, 8, 4, 7, 6]
W = 18
n = len(val)
print("0-1배낭문제(분할 정복): ", knapSack_dc(W, wt, val, n))
print("0-1배낭문제(동적 계획): ", kanpSack_dp(W, wt, val, n))