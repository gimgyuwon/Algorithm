import sys

n, s = map(int, sys.stdin.readline().strip().split())
sequence = list(map(int, sys.stdin.readline().strip().split()))
cnt = 0

def cnt_of_subseqence(idx, sub_sum, blank):
    global cnt 

    if idx == n:
        if sub_sum == s and not blank:
            cnt += 1
        return
    
    cnt_of_subseqence(idx + 1, sub_sum + sequence[idx], False)
    cnt_of_subseqence(idx+1, sub_sum, blank)

cnt_of_subseqence(0, 0, True)
print(cnt)