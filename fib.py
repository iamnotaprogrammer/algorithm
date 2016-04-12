# Uses python3
def calc_fib(n):
    if n == 0:
        return 0
    if n < 3:
        return 1
    else : 
        array = [1,1]
        temp = 0
        for i in range(3,n+1):
            temp = array[0]
            array[1] = array[1] + array[0]
            array[0] = array[1] - array[0]
    return array[1]

n = int(input())
print(calc_fib(n))
