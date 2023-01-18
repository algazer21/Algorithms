# Uses python3
import sys

def optimal_summands(n):
    summands = []
    if n < 3:
        return [n]
    i = 0
    k = 0
    while k+i < n:
        i += 1
        k += i
        summands.append(i)
    
    g = n%k
    
    for j in range(i-g,i):
        summands[j]+=1
         
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    #n = 10   
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
        
