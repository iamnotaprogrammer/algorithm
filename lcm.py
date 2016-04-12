# Uses python3
import sys
def gsd(a,b):
    if a == 0 or b == 0:
        return a+b
    else:
        if a > b:
            return gsd(b,a%b)
        else: return gsd(a,b%a)
def lcm(a, b):
    return a*b// gsd(a,b)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))

