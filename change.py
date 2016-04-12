# Uses python3
import sys

def get_change(n):
    count = 0
    while n >= 0:
        if n - 10 >=0:
            n =n - 10
            count +=1
            continue
        elif n - 5 >=0:
            n =n - 5
            count +=1
            continue
        else:
            n =n - 1
            count +=1 
    return count-1

if __name__ == '__main__':
    n = int(sys.stdin.read())
    print(get_change(n))
