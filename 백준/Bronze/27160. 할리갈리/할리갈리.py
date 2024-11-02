import sys
from collections import defaultdict


def haligarli(n, cards):
    card_dic = defaultdict(int)
    for card in cards:
        fruit, count = card.split()
        card_dic[fruit] += int(count)
    if 5 in card_dic.values():
        return "YES"
    return "NO"


n = int(sys.stdin.readline())
cards = [sys.stdin.readline().strip() for _ in range(n)]
print(haligarli(n, cards))
