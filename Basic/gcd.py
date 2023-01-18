# Uses python3
import sys

def gcd_naive(a, b):
    
    if a == 0 or b == 0:
        return 'error'
    while a%b != 0:
        d = a%b
        a = b
        b = d
    return b  


if __name__ == "__main__":
    #input = sys.stdin.read()
    #a, b = map(int, input.split())
    a = 10
    b = 10
    print(gcd_naive(a, b))
