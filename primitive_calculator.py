# Uses python3
import sys

def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)
def calculation(x):
    arr = [0]*(x+1)
    arr[0] = 0
    ans = list()
    for i in range(1,len(arr)):
        arr[i] = 1+ min(count3(arr,i),count2(arr,i),count1(arr,i))
    while i!=0:
        ind1 = i-1
        ind2 = division(i,2)
        ind3 = division(i,3)
        if ind2 & ind3:
            temp = min((arr[ind1],ind1),(arr[ind2],ind2),(arr[ind3],ind3))
            ans.append(temp[1])
            i = temp[1] 
        elif ind2:
            temp = min((arr[ind1],ind1),(arr[ind2],ind2))
            ans.append(temp[1])
            i = temp[1] 
        elif ind3:
            temp = min((arr[ind1],ind1),(arr[ind3],ind3))
            ans.append(temp[1])
            i = temp[1] 
        else:
            ans.append(ind1)
            i = ind1 
    b = list(reversed(ans[:len(ans)-1]))
    b.append(x)
    return b
def division(i,a):
    if i%a == 0:
        return i//a
    else: return False

    
def count3(arr,i):
    if i == 3:
        return 0
    elif i%3 == 0:
        return arr[i//3]
    elif (i-1)%3 == 0:
        return arr[(i-1)//3]+1
    else :
        return arr[(i-2)//3]+2
def count2(arr,i):
    if i == 2:
        return 0
    elif i%2 == 0:
        return arr[i//2]
    else:
        return arr[(i-1)//2]+1
def count1(arr,i):
    if i == 1:
        return 0
    return arr[i-1]
    

    
input = sys.stdin.read()
n = int(input)
sequence = calculation(n)
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
