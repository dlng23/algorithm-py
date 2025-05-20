n, k = map(int, input().split())
s = []

max_a = n//2
max_k = (n-max_a)*max_a

if k > max_k:
    print (-1)
else:
    for a in range(max_a+1):
        b = n-a
        if a * b >= k:
            break

    s = ['A']*a + ['B']*b
    d = a*b - k
    for i in range(a-1, -1, -1):
        move = min(d, b)
        s.pop(i)
        s.insert(i + move, 'A')
        d -= move
        if d == 0:
            break

    print(''.join(s))