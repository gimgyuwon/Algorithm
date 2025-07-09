import sys

def find_permutation(n):
    if len(result) == n:
        print(*[x+1 for x in result])
        return
    for i in range(n):
        if not used[i]:
            result.append(i)
            used[i] = True

            find_permutation(n)

            result.pop()
            used[i] = False


n = int(sys.stdin.readline().strip())
used = [False] * n
result = []
find_permutation(n)