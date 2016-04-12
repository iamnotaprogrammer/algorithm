# Uses python3
import sys

# def fast_count_segments(starts, ends, points):
#     cnt = list()
#     for el in points:
#         cnt.append(countl - countr)
#         countl,countr = 0,0
#         for l,r in zip(starts,ends):
#             if x > l:
#                 countl +=1
#             if x < r:
#                 countr +=1
# return cnt
def merge2(a , b):
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
def pizdez(starts,ends,points):
    mypoints = list()
    mys = list()
    mye = list()
    answer = list()
    i = 2
    for el in points:
        mypoints.append((el,i))
        i+=1
    for i in range(len(starts)):
        mys.append((starts[i],1))
        mye.append((ends[i],-1))
        
    mypoints.sort(key = lambda x : x[0])
    mys.sort(key = lambda x : x[0])
    mye.sort(key = lambda x : x[0])
    temp = merge2(mys,merge2(mypoints,mye))
    count = 0
    answer = [0]*len(points)
    for el in temp:
        if el[1] <= 1:
            count +=el[1]
        else:
            answer[el[1] - 2] = count 
    return answer
def fast_count_segments(starts, ends, points): 
    mystarts = list()
    myends = list()
    answer = list()
    for i in range(len(starts)):
        mystarts.append((starts[i],1))
        myends.append((ends[i],-1))
    temp = mystarts + myends
    mysegments = quicksort(temp,0,len(temp)-1)
    for el in points:
        count = 0
        temp = bi2(mysegments,el)
        for i in range(temp):
            count += mysegments[i][1]
        answer.append(count)
    return answer


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    starts,ends = list(),list()
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments

    cnt = pizdez(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
