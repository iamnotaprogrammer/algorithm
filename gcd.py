# Uses python3
import sys


def gcd(a,b):
    if a == 0 or b == 0:
        return a+b
    else:
        if a > b:
            return gcd(b,a%b)
        else: 
        	return gcd(a,b%a)

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd(a, b))
