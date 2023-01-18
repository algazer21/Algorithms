# Uses python3
import sys

def get_change(m):
    k = 0                          
    arr = []
    
    while m > 0:
        if m == 1:
            m-= 1
            j = 1
        elif m % 4 == 0:
            m -= 4
            j = 4
        elif m % 3 == 0:
            m -= 3
            j = 3     
        elif (m-1) % 3 == 0:
            m -= 3
            j = 3
        elif (m+1) % 4 == 0 or (m+2) % 4 == 0 and m != 2:
            m -= 4
            j = 4         
        else:
            m -= 1
            j = 1
        arr.append(j)
        k += 1
    
    print(arr)
    return k

if __name__ == '__main__':
    #m = int(sys.stdin.read())
    m = 19
    print(get_change(m))
