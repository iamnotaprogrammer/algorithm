# Uses python3
import sys
import random

def partition3(a, l, r):
    #write your code here
    pass

def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m = partition2(a, l, r)
    randomized_quick_sort(a, l, m - 1);
    randomized_quick_sort(a, m + 1, r);
def qsort(L):
    quicksort(L,0,len(L))

def quicksort(L,start,stop):
    if stop - start < 2: return
    key = L[R.randrange(start,stop)]
    e = u = start
    g = stop
    while u < g:
        if L[u] < key:
            swap(L,u,e)
            e = e + 1
            u = u + 1
        elif L[u] == key:
            u = u + 1
        else:
            g = g - 1
            swap(L,u,g)
    quicksort(L,start,e)
    quicksort(L,g,stop)

def swap(A,i,j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

if __name__ == '__main__':
    input = sys.stdin.read()
    
    R = random.Random(42)
    n, *a = list(map(int, input.split()))
    qsort(a)
    for x in a:
        print(x, end=' ')
