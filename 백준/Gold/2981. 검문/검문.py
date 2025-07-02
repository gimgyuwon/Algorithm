import sys
from itertools import combinations
from math import gcd
from functools import reduce

numbers = list(map(int, [line.strip() for line in sys.stdin.readlines()]))
numbers = numbers[1:]

def get_multiple(numbers):
    return reduce(gcd, numbers)

def get_divisors(gcd):
    divisors = set()
    for i in range(2, int(gcd**0.5) + 1):
        if gcd % i == 0:
            divisors.add(i)
            divisors.add(gcd//i)
    divisors.add(gcd)
    return sorted(divisors)

diffs = set(abs(a - b) for a, b in combinations(numbers, 2))
gcd = get_multiple(diffs)
print(' '.join(map(str, get_divisors(gcd))))