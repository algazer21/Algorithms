# Uses python3
import sys

def lcm_naive(a, b):
    m = a*b   
    if a == 0 or b == 0:
        return 'error'
    while a%b != 0:
        d = a%b
        a = b
        b = d
    return int(m/b)


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))

