import sys

input = sys.stdin.readline

def find_idx(word):
    alphabet = [-1] * 26
    for idx, ch in enumerate(word):
        alphabet_idx = ord(ch) - ord('a')
        if alphabet[alphabet_idx] == -1:
            alphabet[ord(ch) - ord('a')] = idx
    return alphabet

word = input().strip()
print(*find_idx(word))
