# Uses python3
import sys

def optimal_summands(n):
    summa = 0
    summands = []
    for i in range(1,n+1):
        summa +=i
        if summa ==n:
            summands.append(i)
            return summands
        if  n - summa > i:
            summands.append(i)
        else:
            summa -= i
            continue

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
