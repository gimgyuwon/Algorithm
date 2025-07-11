import sys
from functools import reduce

# find GCD
def GCD(x, y):
    while y != 0:
        x, y = y, x%y
    return x

children, hero = map(int, sys.stdin.readline().strip().split())
children_loc = map(int, sys.stdin.readline().strip().split())

diff_list = [abs(i-hero) for i in children_loc]


result = reduce(GCD, diff_list)

print(result)