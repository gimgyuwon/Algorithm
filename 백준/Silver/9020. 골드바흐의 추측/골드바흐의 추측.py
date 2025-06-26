
import sys

def sieve(max_n):
    is_prime = [False]*2 + [True] * max_n
    for i in range(2, int(max_n**0.5)+ 1):
        if is_prime[i]:
            for j in range(i*i, max_n + 1, i):
                is_prime[j] = False
    return is_prime

def least_gap(pairs):
    min_gap = float('inf')
    min_pair = None
    for a, b in pairs:
        gap = abs(a-b)
        if gap < min_gap:
            min_gap = gap
            min_pair = (a, b)
    return min_pair


def largest_prime_less_than(n, is_prime_arr):
    lst = []
    for i in range(2, n//2 + 1):
        if is_prime_arr[i] and is_prime_arr[n-i]:
            lst.append((i, n-i))
    return least_gap(lst)


t = int(sys.stdin.readline())
inputs = [int(sys.stdin.readline().strip()) for _ in range(t)]
max_n = max(inputs)
is_prime_arr = sieve(max_n)

result = []

for n in inputs:
    a, b = largest_prime_less_than(n, is_prime_arr)
    result.append((a, b))

for a, b in result:
    print(a, b)