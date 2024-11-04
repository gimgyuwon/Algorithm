import sys
from collections import defaultdict


def is_work_fair(N, week):
    time_per_person = defaultdict(int)
    hours = [4, 6, 4, 10]

    for i in range(4 * N):
        hour_group = i % 4
        for person in week[i]:
            if person != "-" and person:
                time_per_person[person] += hours[hour_group]

    if len(time_per_person) == 0:
        return "Yes"

    time_values = list(time_per_person.values())

    if max(time_values) - min(time_values) <= 12:
        return "Yes"

    return "No"


N = int(sys.stdin.readline().strip())
week = [line.strip().split() for line in [sys.stdin.readline().strip() for _ in range(4 * N)]]
print(is_work_fair(N, week))
