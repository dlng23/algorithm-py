def hanoi_tower(n, fr, tmp, to) :
    if (n==1):
        print("원판 1: %s --> %s" % (fr, to))
    else: 
        hanoi_tower(n-1, fr, to, tmp) # 단계 1
        print("원판 %d: %s --> %s" % (n, fr, to)) # 단계 2
        hanoi_tower(n-1, tmp, fr, to) # 단계 3