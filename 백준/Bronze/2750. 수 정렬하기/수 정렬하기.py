import sys

def sorting_n(lst):
    return sorted(lst)

n = int(sys.stdin.readline().strip())
number_lst = map(int, sys.stdin.read().splitlines())

print('\n'.join(map(str, sorting_n(number_lst))))