#Uses python3

import sys

def compare(c,d):
    if c == d:
        return False
    
    g = [str(c),str(d)]
    h = [str(d),str(c)]
    g = int(''.join(g))
    h = int(''.join(h))
    
    if g>h:
        return True
    else:
        return False
    

def largest_number(a):
    #write your code here
    res = []
    n = len(a)
    for j in range(n):
        m = a[0]
        k= 0
        for i in range(1,n-j):
            mm = compare(a[i],m)
            if  mm == True:               #a[i] > m:
                m = a[i]
                k = i
        res.append(m)
        print(res)
        if len(res) < n:
            a.pop(k)
            
    return int(''.join(list(map(str,res))))

if __name__ == '__main__':
    #input = sys.stdin.read()
    #data = input.split()
    #a = data[1:]
    a = [20,202,1,2,34,0]
    print(largest_number(a))
    
