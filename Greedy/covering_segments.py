# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def getKey(item):
    return item[1]

def optimal_points(segments):
    points = []
    
    
    i = 0
    
    while len(segments) != 0:
        j = 0
        points.append(segments[0].end) 
        segments.pop(0)
        
        while len(segments) != j:
        
            if segments[j].start <= points[i]:
                segments.pop(j)
            elif segments[j].start > points[i]:
                j += 1
            
        i+=1
     
    return points  
    

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(sorted(segments,key = getKey))
    print(len(points))
    print(*points)
