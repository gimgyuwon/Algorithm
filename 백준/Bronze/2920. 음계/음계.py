import sys

def scale(lst):
    if lst == sorted(lst):
        return 'ascending'
    elif lst == sorted(lst, reverse=True):
        return 'descending'
    else:
        return 'mixed'

input = sys.stdin.readline
lst = list(map(int, input().strip().split()))

print(scale(lst))