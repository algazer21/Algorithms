import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n
    a,b = 0,1
    for i in range(1,n):
        f = (a%10) + (b%10)
        a = b%10
        b = f%10   

    return f % 10

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
