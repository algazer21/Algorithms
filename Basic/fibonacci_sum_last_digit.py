# Uses python3
import sys

def fibonacci_sum_naive(n):
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
    #input = sys.stdin.read()
    #n = int(input)
    n = 5
    print(fibonacci_sum_naive(n))
