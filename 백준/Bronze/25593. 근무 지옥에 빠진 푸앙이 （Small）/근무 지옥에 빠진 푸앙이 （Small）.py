import sys
from collections import defaultdict

def is_fair(person_schedule):
    max_time = max(person_schedule.values())
    min_time = min(person_schedule.values())
    return max_time - min_time <= 12

def solution(schedule):
    person_schedule = defaultdict(int)
    work_hour = [4, 6, 4, 10]
    for week_idx, person in enumerate(schedule):
        for part in person:
            if part == "-":
                continue
            person_schedule[part] += work_hour[week_idx % 4]

    if not person_schedule:
        return "Yes"
    if is_fair(person_schedule):
        return "Yes"
    else:
        return "No"

week = int(sys.stdin.readline().strip())
schedule = [sys.stdin.readline().strip().split() for _ in range(4*week)]

print(solution(schedule))
