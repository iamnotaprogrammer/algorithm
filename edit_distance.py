# Uses python3
def distance(a,b):
    arr = [[0 for x in range(len(a)+1)] for x in range(len(b)+1)]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j] = Dij(i,j,arr,a,b)
    return arr[i][j]
def Dij(i,j,arr,a,b):
    k,u = i-1,j-1
    if i<=0:
        return j
    elif j<=0:
        return i
    elif a[u] == b[k]:
          return min(arr[i][j-1]+1,arr[i-1][j]+1,arr[i-1][j-1])
    else:
        return min(arr[i][j-1]+1,arr[i-1][j]+1,arr[i-1][j-1]+1)

if __name__ == "__main__":
    print(distance(input(), input()))
