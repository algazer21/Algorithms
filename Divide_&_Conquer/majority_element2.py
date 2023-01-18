# Uses python3
import sys
import random as ram


def contador(a,y,mm):
    f = 0
    for i in range(0,mm+1):
        if a[i] == y:
            f+=1
    return f
            

def get_majority_element(a):
    m = len(a)-1
    d = int(n/2)
    for i in range(15):
        k = ram.randint(0, m)
        g = contador(a,a[k],m)
        if g > d:
            return 1
    
    return 0
   

if __name__ == '__main__':
    #input = sys.stdin.read()
    #n, *a = list(map(int, input.split()))
    a = [512766168,71738375,5,126144732,5,573799007,5,5,5,405079772]
    n = len(a)
    print(get_majority_element(a))

    
