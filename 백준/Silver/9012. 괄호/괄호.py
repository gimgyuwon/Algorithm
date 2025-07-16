import sys

def validate_ps(ps):
    right = 0
    left = 0
    ps = list(ps)
    while len(ps) > 0:
        last = ps.pop()
        if last == ")":
            right += 1
        else:
            if right > 0:
                right -= 1
            else:
                left += 1
    if (right == 0 and left == 0):
        return "YES"
    return "NO"


input = sys.stdin.read().splitlines()[1:]

for part in input:
    print(validate_ps(part))
