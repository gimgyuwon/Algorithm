import sys

input = sys.stdin.readline
n = int(input().strip())
num_lst = list(map(int, input().strip().split()))

def coordinate_comparasion(lst):
    sorted_lst = sorted(set(lst))
    coord_map = {num: i for i, num in enumerate(sorted_lst)}
    return [coord_map[num] for num in lst]

print(*coordinate_comparasion(num_lst))