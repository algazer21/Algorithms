# Uses python3
import sys

def fibonacci_partial_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    su = 1
    rem = n%60
    
    if rem == 0:
        return 0

    for i in range(1,rem):
        previous, current = current, previous + current
        su += current 

    return su%10


if __name__ == '__main__':
    input = sys.stdin.read();
    m, n = map(int, input.split())
    if m == 0 or n == 0:
        print((fibonacci_partial_sum_naive(n)-fibonacci_partial_sum_naive(m))%10)
    else:
        print((fibonacci_partial_sum_naive(n)-fibonacci_partial_sum_naive(m-1))%10)