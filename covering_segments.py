# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')
def cover(seg,n):
    ar = list()
    numbers = []
    answer = [False for i in range(n)]
    for el in seg:
        if el[1] >0:
            numbers.append(el[2])
        else:
            if answer[el[2]]:
                continue
            else :
                answer[el[2]] = True
                numbers.remove(el[2])
                ar.append(el[0])
                for el in numbers:
                    answer[el] = True
                numbers = []    
    return ar
def merge(a , b):
    answer = list()
    i,j = 0,0
    while True:
        if i >=len(a):
            return answer + b[j:]
        if j >= len(b):
            return answer + a[i:]
        if a[i][0] <= b[j][0]:
            answer.append(a[i])
            i += 1
        else:
                answer.append(b[j])
                j += 1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    new_starts = list()
    new_ends = list()
    for i in range(len(segments)):
        new_starts.append((segments[i][0],1,i))
        new_ends.append((segments[i][1],-1,i))
    new_starts.sort()
    new_ends.sort()
    seg = merge(new_starts,new_ends)
    points = cover(seg,n)
    print(len(points))
    for p in points:
        print(p, end=' ')
