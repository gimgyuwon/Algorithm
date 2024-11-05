import sys
import math


def password(pw_list):
    for word in pw_list:
        if word[::-1] in pw_list:
            ans_len = len(word)
            ans_middle = word[math.floor(len(word)//2)]
    print(ans_len, ans_middle)


n = int(sys.stdin.readline())
pw_list = [sys.stdin.readline().strip() for _ in range(n)]
password(pw_list)