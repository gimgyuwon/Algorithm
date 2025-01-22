import sys

def get_winning_rate(game_num, win_num):
    rate = (win_num * 100) // game_num
    return rate

def game(game_num, win_num):
    start, end = 1, game_num
    original_rate = get_winning_rate(game_num, win_num)
    result = 0

    if original_rate >= 99:
        return -1
    
    while start <= end:
        mid = (start + end) // 2
        temp_rate = get_winning_rate(game_num+mid, win_num+mid)

        if temp_rate > original_rate:
            end = mid - 1
            result = mid
        else:
            start = mid + 1
    return result

game_num, win_num = map(int, sys.stdin.readline().strip().split(" "))
print(game(game_num, win_num))