import sys

def word_game(case):
    for word in case:
        result = word[0::2]
        result_pair = word[1::2]

        if len(word) % 2 != 0:
            even = result
            odd = result_pair
            result = even + odd
            result_pair = odd + even

        print(result)
        print(result_pair)

n = int(sys.stdin.readline().strip())
case = [sys.stdin.readline().strip() for _ in range(n)]

word_game(case)