import sys

def hanoi_top(n, start, end):
    if n == 1:
        print(f"{start} {end}")
        return
    mid = 6 - start - end
    hanoi_top(n-1, start, mid)
    print(f"{start} {end}")
    hanoi_top(n-1, mid, end)

n = int(sys.stdin.readline().strip())
print(2**n - 1)
if n <= 20:
    hanoi_top(n, 1, 3)