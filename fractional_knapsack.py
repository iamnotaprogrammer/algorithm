# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    arr = list()
    for w,v in zip(weights,values):
        arr.append([w,v,v/w])
    arr.sort(key = lambda x : x[2],reverse = True)
    i=0
    while i < len(arr):
        if capacity <=0:
               return value
        k = capacity // arr[i][0]
        a = min(arr[i][0],capacity)
        value +=a*arr[i][2]
        capacity -=a
        i+=1
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
