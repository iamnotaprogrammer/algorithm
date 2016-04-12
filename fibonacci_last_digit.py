# Uses python3
import sys

def get_fibonacci_last_digit(n):
    if n < 3:
        return 1
    else : 
        array = [1,1]
        temp = 0
        for i in range(3,n+1):
            temp = array[0]
            array[1] = (array[1] + array[0])%10
            array[0] = (array[1] - array[0])%10
    return array[1]

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit(n))
