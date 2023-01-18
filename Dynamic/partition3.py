# Uses python3
import sys
import itertools

def reconstruction(u,W,w):   
    i = W
    j = len(w)
    v = [0]*j
    while 1:
        if u[j][i] != u[j-1][i]:
            v[j-1] = 1
            i-=w[j-1]
            j-=1
        elif u[j][i] == u[j-1][i]:
            j-=1
        if u[j][i] == w[j-1]:
            v[j-1] = 1
            break
        
    for i in reversed(range(len(v))):
        if v[i] == 1:
            w.pop(i)
    return w      
    

def optimal_weight(W, w):
    a = [0]*(W+1)
    b = [0]*(W+1)
    c = [[0]*(W+1)]
    n = len(w)
    for i in range(1,n+1):
        for j in range(1,W+1):
            if w[i-1]>j:
                b[j] = a[j]
            else:
                b[j] = max(w[i-1]+a[j-w[i-1]],a[j])
        a = b
        c.append(a)
        b = [0]*(W+1)
        #print(a)
    l = reconstruction(c, W, w)
                        
    return a[len(a)-1],l


def partition3(A):
    m = sum(A)
    if m%3 != 0 or len(A)<3:
        return 0
    m = m//3
    k,A = optimal_weight(m, A)
    #print(m,A)
    if k != m:
        return 0
    k2,A = optimal_weight(2*m, A)
            
    if k == k2//2:
        return 1

    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    #A = [17,59,34,57,17,23,67,1,18,2,59]
    #A = [30]
    print(partition3(A))

