import sys
from collections import deque

def cutting_iron_bar(parentheses):
    stack = 0
    cutting = 0
    while parentheses:
        # cutting iron bar
        if parentheses[0] == '(' and parentheses[1] == ')':
            cutting += stack
            parentheses.popleft()
        # closed right parenthese
        elif parentheses[0] == ')':
            cutting += 1
            stack -= 1
        # open left parenthese
        else:
            stack += 1
        parentheses.popleft()
    print(cutting)

parentheses = list(sys.stdin.readline())
parentheses = deque(parentheses)
cutting_iron_bar(parentheses)
