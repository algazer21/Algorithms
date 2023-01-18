# Uses python3
import sys

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
    return v      
    

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
        print(b)
        a = b
        c.append(a)
        b = [0]*(W+1)
    #print(reconstruction(c, W, w))                    
    return a[len(a)-1]

if __name__ == '__main__':
    #input = sys.stdin.read()
    #W, n, *w = list(map(int, input.split()))
    w = [1,4,8]
    W = 10
    print(optimal_weight(W, w))
