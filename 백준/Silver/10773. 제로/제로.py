import sys

def zero(lst):
    result = []
    for part in lst:
        if part == 0:
            result.pop()
        else:
            result.append(part)
    return print(sum(result))

lst = list(map(int, sys.stdin.read().splitlines()[1:]))

zero(lst)