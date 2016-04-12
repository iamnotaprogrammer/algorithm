# Uses python3
import sys

def get_majority_element(seq, left, right):
    maj = len(seq)//2+1
    mydict = dict()
    for el in seq:
        if mydict.get(el,0) == 0:
            mydict[el] = 1
        else:
            mydict[el] +=1
    ans = max(mydict.items(),key = lambda x : x[1]) 
    if ans[1] >= maj:
        return 1
    else:
        return -1
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
