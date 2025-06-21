def fib_dp_mem(n):
    if (mem[n]==None):
        if n<2:
            mem[n]=n
        else: 
            mem[n]=fib_dp_mem(n-1)+fib_dp_mem(n-2)
    return mem[n]

def fib_dp_tab(n):
    f = [None] + (n+1)
    f[0] = 0
    f[1] = 1
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]