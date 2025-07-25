import sys
from collections import deque

def card(card_num):
    card_list = deque(range(1, card_num + 1))
    while len(card_list) > 1:
        card_list.popleft()
        card_list.append(card_list.popleft())
    print(card_list[0])

card_num = int(sys.stdin.readline().strip())

card(card_num)