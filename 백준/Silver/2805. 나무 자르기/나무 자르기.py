import sys

input = sys.stdin.read
data = input().splitlines()
n, m = map(int, data[0].split())
tree_lst = list(map(int, data[1].split())
)

def cal_cut(tree_lst, cutting_hgt):
    # cutting_hgt : 커팅하는 m (ex. 15m)
    # cut: 자른 양
    cut = 0
    for tree in tree_lst:
        if tree > cutting_hgt:
            cut += (tree - cutting_hgt)
        # print("cutting_hgt", cutting_hgt, "cut", cut)
    return cut

def cutting_tree (tree_lst, goal) :
    start, end = 0, max(tree_lst)

    while start <= end:
        # 중간값 계산
        mid = (start + end) // 2
        # 나무 자르기
        cut = cal_cut(tree_lst, mid)
        # goal과 cut을 비교
        if cut >= goal:
            start = mid + 1
        else:
            end = mid - 1
    return end

print(cutting_tree(tree_lst, m))