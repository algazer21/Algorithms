# Uses python3
from sys import stdin

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    rem = n%60
    
    if rem == 0:
        return 0

    for i in range(1,rem):
        previous, current = current, previous + current

    return current%10

if __name__ == '__main__':
    n = int(stdin.read())
    #n = 3
    print((fibonacci_sum_squares_naive(n)*fibonacci_sum_squares_naive(n+1))%10)
