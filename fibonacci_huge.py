# Uses python3
import sys

def get_fibonaccihuge(n, m):
    array = [0,1]
    array1 = [0,1]
    for i in range(2,n+1):
        temp = array[1]
        array[1] = (array[1] + array[0])%m
        array[0] = (temp)%m
        array1.append(array[1])
        length_array1 = len(array1)
        if length_array1%2 == 0 :
            answer = True
            for i in range(length_array1//2):                
                if array1[i] != array1[i+length_array1//2]:
                    answer = False
                    break
            if answer:
                return array1[(n%(length_array1//2))]
    return array[1]%m

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonaccihuge(n, m))
