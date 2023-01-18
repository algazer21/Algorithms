# Uses python3
import sys

def binary_search(a, x):
    l, r = 0, len(a)
    j = False
    
    while j == False:
        b = int(l + ((r-l)/2))
        c = int((r-l)/2)
        
        if x == a[b]:
            return b
        if x < a[b]:
            r = r - c
            if x == a[b-1]:
                return b-1
        if x > a[b]:
            l = l + c
            
        if r-l == 1:
            return -1
    
    return b



if __name__ == '__main__':
    
    #input = sys.stdin.read()
    #data = list(map(int, input.split()))
    gg = '5 1 5 8 12 13 5 8 1 23 1 11'
    data = list(map(int, gg.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        print(binary_search(a, x), end = ' ')
        
