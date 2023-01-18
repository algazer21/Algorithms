# Uses python3
import sys

def optimal_sequence(nn):
    m = nn
    sequence = []
    arr = [1,1,1]
    for i in range(4,m+1):
        n = i
        k = 1
        m = 100000
        if n % 3 == 0:
            kk = arr[n//3 -1]
            m = arr[n//3-1]
             
        if n % 2 == 0:
            if arr[n//2-1]<m:
                kk = arr[n//2 -1]
                m = arr[n//2-1]
                
        if arr[n-2] < m:
            kk = arr[n-2] 
        k+= kk
        arr.append(k)
        
        
    n = nn
        
    while n >= 1:
        sequence.append(n)
   
        m = 10000000
        if n % 3 == 0:
            m = arr[n//3-1]
            j = n//3
            
        if n % 2 == 0:
            if arr[n//2-1] < m:
                m = arr[n//2-1]
                j = n//2
                
        if arr[n-2] < m:
            j = n-1
            
        n = j
        
    #print(arr[nn-1])
    return reversed(sequence)

#input = sys.stdin.read()
#n = int(input)
n = 96234
sequence = list(optimal_sequence(n))

print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
