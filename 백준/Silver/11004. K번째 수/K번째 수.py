import sys
import random


def quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]

    pivot = random.choice(arr)
    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]

    if k < len(lows):
        return quickselect(lows, k)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots))


input_data = sys.stdin.readline().strip()
num, k = map(int, input_data.split())
num_list = list(map(int, sys.stdin.readline().strip().split()))

print(quickselect(num_list, k - 1))
