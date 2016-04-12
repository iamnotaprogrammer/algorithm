# Uses python3
import sys
def merge(a , b):
    answer = list()
    i,j = 0,0
    count = 0
    while True:
        if i >=len(a):
            return answer + b[j:],count
        if j >= len(b):
            return answer + a[i:],count
        if a[i] <= b[j]:
            answer.append(a[i])
            i += 1
        else:
                answer.append(b[j])
                j += 1
                count += len(a)-i
                
def mergesort(arr):
    if len(arr) == 1:
        return arr,0
    else:
        mid = len(arr)//2
        left, cl = mergesort(arr[:mid])
        right, cr = mergesort(arr[mid:])
        result, c = merge(left,right)
        count = cl + cr + c
        return result,count
    
def count(arr):
    return mergesort(arr)[1]



def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    #write your code here
    return number_of_inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(count(a))
