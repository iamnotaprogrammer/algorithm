# Uses python3
import sys

def binary_search(a, x):
    mid = (len(arr)//2)+1
    left = 0
    right = len(arr)-1
    while True:
        print(left,mid,right)
        if arr[mid] == x:
            print(mid)
            break
        if arr[mid] > x:
            right = mid
            mid = left + (right - left)//2     
        if arr[mid] < x:
            left = mid
            mid = left + (right - left)//2

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(linear_search(a, x), end = ' ')
