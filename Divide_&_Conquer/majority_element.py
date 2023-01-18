# Uses python3
import sys

def major(a,k,m):
    f = 0
    h = 0
    for i in range(k,m+1):
        for j in range(k,m+1):
            if a[i] == a[j]:
                f +=1
        if f > h:
            g = a[i]
            h = f
        f = 0
    return g,h


def contador(a,y,k,m):
    f = 0
    for i in range(k,m+1):
        if a[i] == y:
            f+=1
    return f
            

def get_majority_element(a):
    d = int(n/2)
    if d == 0:
        return 1
       
    g,gg = major(a,0,d-1)
    h,hh = major(a,d,n-1)
    
    if g == h and gg+hh > d:
        return 1
    
    if hh > gg:
        hh2 = contador(a,h,0,d-1)
        if hh+hh2 > d:
            return 1
    
    if hh < gg:
        gg2 = contador(a,g,d,n-1)
        if gg+gg2 > d:
            return 1
    
    return 0

def divide(a):
    while 
    

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    #a = [1,2,3,1]
    #n = len(a)
    print(get_majority_element(a))

    
