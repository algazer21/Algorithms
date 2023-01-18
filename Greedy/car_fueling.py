# python3
import sys


def compute_min_refills(distance, tank, stops):
    b = False
    i = 0
    m = 0
    road = 0
    aux = stops[0]
    
    while road < distance-tank:
        while i < len(stops) and aux-road <= tank :
            b = True
            i+=1
            if i < len(stops):
                aux = stops[i]
            
        if b == False:
            return -1
        
        m+=1
        road = stops[i-1]
        b = False
    
    return m

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    #d = 200
    #m = 250
    #stops = [100,150]
    print(compute_min_refills(d, m, stops))
