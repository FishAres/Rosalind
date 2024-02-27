data = (36, 4)

def fib_n(n, k):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (fib_n(n-1, k) + k*fib_n(n-2, k))
    
print(fib_n(data[0], data[1]))