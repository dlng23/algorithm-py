def factorial_iter(n) : 
    rsult = 1
    for k in range(2, n+1) : 
        result = result * k
        return result
    
def factorial(n) :
    if n==1 : 
        return 1
    else : 
        return n * factorial(n-1)