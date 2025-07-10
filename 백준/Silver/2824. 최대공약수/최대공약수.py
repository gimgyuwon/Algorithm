import sys
from functools import reduce

def multiple(x, y):
    return x*y

def GCD(m, n):
    while n != 0:
        m, n = n, m%n
    return m

input = sys.stdin.readlines()
m, n = reduce(multiple, map(int, input[1].strip().split())), reduce(multiple, map(int, input[3].strip().split()))
print(str(GCD(m, n))[-9:])