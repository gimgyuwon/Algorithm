import sys
import math

n, m = map(int, sys.stdin.readline().strip().split())

print(math.comb(n, m))