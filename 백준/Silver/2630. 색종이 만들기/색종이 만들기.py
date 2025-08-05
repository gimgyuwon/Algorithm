import sys

white_cnt = 0
blue_cnt = 0

def find_same_color_area(y, x, size):
    global white_cnt, blue_cnt
    color = confetti_lst[y][x]
    same = True
    for i in range(y, y+size):
        for j in range(x, x+size):
            if color != confetti_lst[i][j]:
                same = False
                break
        if not same:
            break;

    if same:
        if color == 0:
            white_cnt += 1
        else:
            blue_cnt += 1
        return
    
    else:
        half = size // 2
        find_same_color_area(y, x, half)
        find_same_color_area(y, x+half, half)
        find_same_color_area(y+half, x, half)
        find_same_color_area(y+half, x+half, half)

n = int(sys.stdin.readline().strip())
confetti_lst = [list(map(int, line.split())) for line in sys.stdin.read().splitlines()]

find_same_color_area(0, 0, n)

print(white_cnt)
print(blue_cnt)
