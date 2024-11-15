from collections import deque
import sys

def max_queue_size(n, A):
    queue = deque()  # 줄을 나타내는 큐
    max_count = 0  # 대기 중인 학생 수의 최댓값
    last_student = None  # 최대 학생 수일 때 맨 뒤에 있는 학생 번호

    for command in A:
        if command[0] == 1:  # 학생이 줄을 서는 경우
            student_id = command[1]
            queue.append(student_id)
            # 최대 대기 인원 수 갱신
            if len(queue) > max_count:
                max_count = len(queue)
                last_student = student_id
            elif len(queue) == max_count:
                last_student = min(last_student, student_id)

        elif command[0] == 2:  # 식사 1인분 준비로 학생이 줄에서 나가는 경우
            queue.popleft()

    print(max_count, last_student)

# 입력 처리
n = int(sys.stdin.readline().strip())
A = []

for _ in range(n):
    line = list(map(int, sys.stdin.readline().strip().split()))
    A.append(line)

max_queue_size(n, A)
