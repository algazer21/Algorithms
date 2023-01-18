def fib(n):
    if n <= 1:
        return n
    else:
        a,b = 0,1
        for i in range(1,n):
            f= a + b
            a = b
            b = f   
        return f

#m = int(input())
m = 5
print(fib(m))