import sys
import operator

op_map = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '//': operator.floordiv,
    '%': operator.mod,
    '**': operator.pow,
}

def rps_to_ps(rps):
    stack = []
    for token in rps:
        if isinstance(token, int):
            stack.append(token)
        else:
            b = stack.pop()
            a = stack.pop()
            result = op_map[token](a, b)
            stack.append(result)
    return print(f"{stack[0]:.2f}")


input = sys.stdin.readline
n = int(input())
expr = input().strip()

value_map = {}
for i in range(n):
    value_map[chr(ord('A') + i)] = int(input())

rps = []
for ch in expr:
    if ch.isalpha():
        rps.append(value_map[ch])
    else:
        rps.append(ch)

rps_to_ps(rps)
