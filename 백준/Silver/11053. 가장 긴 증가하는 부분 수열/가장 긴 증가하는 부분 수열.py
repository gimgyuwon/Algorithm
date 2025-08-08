import sys
import bisect

input = sys.stdin.readline

def longest_increasing_subsequence(seq):
    lis = []
    for num in seq:
        pos = bisect.bisect_left(lis, num)
        if pos == len(lis):
            lis.append(num)
        else:
            lis[pos] = num
    return len(lis)

n = int(input())
seq = list(map(int, input().strip().split()))

print(longest_increasing_subsequence(seq))