def ab(k, n):
    ab = [[0] * (n + 1) for _ in range(k + 1)]

    for i in range(1, n + 1):
        ab[0][i] = i

    for j in range(1, k + 1):
        for i in range(1, n + 1):
            ab[j][i] = ab[j][i - 1] + ab[j - 1][i]

    return ab[k][n]

tc = int(input())
for _ in range(tc):
    k = int(input())
    n = int(input())
    print(ab(k, n))