#Uses python3

import sys

def max_dot_product(a, b):
    a.sort(reverse=True)
    b.sort(reverse=True)
    res = 0
    for i in range(n):
        print(a[i],b[i])
        res += a[i] * b[i]
    return res

if __name__ == '__main__':
    #input = sys.stdin.read()
    #data = list(map(int, input.split()))
    #n = data[0]
    #a = data[1:(n + 1)]
    #b = data[(n + 1):]
    a = [20,30,10]
    b = [5,2,3]
    n = len(a)
    
    print(max_dot_product(a, b))
    
