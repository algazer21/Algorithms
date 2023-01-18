# Uses python3
# Pisano Period
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    j = False
    arrM = [previous,current]

    for i in range(2,m*m):
        previous, current = current, previous + current
        arrM.append(current%m)

        if arrM[i] == 0:
            h = i
            j = True
        elif arrM[i] == 1 and j == True:
            break
        elif arrM[i] != 1 and j == True:
            j = False
        

    return arrM[n%h]

if __name__ == '__main__':
    #input = sys.stdin.read();
    #n, m = map(int, input.split())
    n = 40
    m = 3
    print(get_fibonacci_huge_naive(n, m))
