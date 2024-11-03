import sys


def sing(sing_num, attempt_num, sing_list, problem):
    # -1 = !
    title = "title"
    for i in range(0, attempt_num):
        ans = -1
        pitch = problem[i].replace(" ", "")
        # print(pitch, 'pitch')
        for j in range(0, sing_num):
            if pitch == sing_list[j][2][:3]:
                ans += 1
                title = sing_list[j][1]
                # print('title', title, pitch)
        if ans == -1:
            print("!")
        if ans == 0:
            print(title)
        if ans > 0:
            print("?")


sing_num, attempt_num = map(int, sys.stdin.readline().split())
sing_list = [
    [part.replace(" ", "") for part in sys.stdin.readline().strip().split(" ", maxsplit=2)]
    for _ in range(sing_num)
]
# print("sing_list: ", sing_list)

problem = [sys.stdin.readline().strip() for _ in range(attempt_num)]
# print(problem)

sing(sing_num, attempt_num, sing_list, problem)
