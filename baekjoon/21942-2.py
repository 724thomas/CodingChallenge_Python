# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

import sys
from datetime import datetime, timedelta
from collections import defaultdict

# sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()


def solution(n, duration, penalty, logs):
    dur_day, dur_time = duration.split("/")
    day = int(dur_day)
    hour, minute = map(int, dur_time.split(":"))

    def calc_fee(borrow_time, return_time):
        datetime_format = "%Y-%m-%d %H:%M"
        borrowed_time = datetime.strptime(borrow_time, datetime_format)
        returned_time = datetime.strptime(return_time, datetime_format)

        max_return_time = borrowed_time + timedelta(days=day, hours=hour, minutes=minute)

        if returned_time <= max_return_time: return 0

        overdue_minutes = (returned_time - max_return_time).total_seconds() // 60
        return overdue_minutes * penalty

    history = defaultdict(dict)
    total_penalty = defaultdict(int)

    for log in logs:
        date, time, part, name = log.split()
        date_time = date + " " + time

        if part not in history[name]:
            history[name][part] = date_time
        else:
            borrowed_time = history[name].pop(part)
            total_penalty[name] += calc_fee(borrowed_time, date_time)

    ans = [(name, total_penalty[name]) for name in total_penalty if total_penalty[name] > 0]
    if not ans:
        print(-1)
        exit()
    ans.sort(key=lambda x: x[0])
    for a in ans:
        print(a[0], str(int(a[1])))


if __name__ == '__main__':
    n, duration, penalty = input().strip().split()
    n = int(n)
    logs = [input().strip() for _ in range(n)]
    solution(n, duration, int(penalty), logs)
