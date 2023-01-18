# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    new = []
    w = []
    v = []
    for j in range(n):
        m = values[0]/weights[0]
        k = 0
        for i in range(1,n-j):
            
            if values[i]/weights[i] > m:
                m = values[i]/weights[i]
                k = i           
        new.append(m)
        w.append(weights[k])
        v.append(values[k])
        m = 0   
        if len(new) < n:
            values.pop(k)
            weights.pop(k)
            

    for i in range(n):
        if capacity == 0:
            return value
        elif w[i] < capacity:
            capacity -= w[i]
            value += v[i]
        else:
            value += v[i]*capacity/w[i]
            capacity = 0

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
