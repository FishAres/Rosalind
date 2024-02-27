data = (6, 3)

def fib_mortal(n, k):
    if n == 0:
        return 0
    elif n in [1, 2]:
        return 1
    else:
        return fib_mortal(n-1, k) - k*fib_mortal(n-2, k)
    
print(fib_mortal(data[0], data[1]))