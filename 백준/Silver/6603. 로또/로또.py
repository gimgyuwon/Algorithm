import sys

def rotto (start, path, n, r):
    if len(path) == r:
        print(' '.join(map(str, path)))
        return
    for i in range(start, n):
        rotto(i+1, path + [arr[i]], n, r)

lst = sys.stdin.readlines()
lst = [list(map(int, line.strip().split())) for line in lst]

for line in lst:
    if line[0] == 0:
        break
    k = line[0]
    arr = line[1:]
    rotto(0, [], k, 6)
    print()