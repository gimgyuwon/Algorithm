import sys
import math

def solution(pw_lst):
    for pw in pw_lst:
        if pw[::-1] in pw_lst:
            len_pw= len(pw)
            middle_pw = pw[(math.floor(len(pw))//2)]
            print(len_pw, middle_pw)
            break

pw_len = int(sys.stdin.readline())
pw_lst = [sys.stdin.readline().strip() for _ in range(pw_len)]
solution(pw_lst)
