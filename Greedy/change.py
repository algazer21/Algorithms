# Uses python3
import sys

def get_change(m):
    d = int(m/10)
    r = m%10
    c = int(r/5)
    r = m%5
    
    return d+c+r

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
