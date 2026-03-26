# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 / 알고리즘 :

'''


import sys
#sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()

def solution(s, e, q):
    start_time = serialize(s)
    end_time = serialize(e)
    q_time = serialize(q)

    entered = set()
    attended = set()

    while True:
        log = input()
        if log == '':
            break
        time, name = log.split()
        time = serialize(time)
        if time <= start_time:
            entered.add(name)
        elif end_time <= time <= q_time:
            if name in entered:
                attended.add(name)
    return len(attended)

def serialize(time: str) -> int:
    hour, minute = map(int, time.split(':'))
    return hour * 60 + minute

def deserialize(time: int) -> str:
    hour, minute = time // 60, time % 60
    return f'{hour:02d}:{minute:02d}'

if __name__ == '__main__':
    s, e, q = map(str, input().split())
    print(solution(s, e, q))

# n = int(input().rstrip())
#
# n, m = map(int, input().split())
# n, m = list(map(int, input().split()))
# a = [c for c in input().strip()]
#
# s = input().rstrip()

# arr = list(map(int, input().strip().split()))
# arr = tuple(map(int, input().split()))
# integer_list = [int(num) for num in input().split()]
# dp = [[0 for _ in range(n)] for _ in range(n)]
# dp = [[0 for j in range(n)] for i in range(n)]
# grid = [list(input().rstrip()) for _ in range(n)] # "aaa" "bbb"
# grid = list(list(map(int, input().split())) for _ in range(n)) # "0 0 0 0", "0 0 0 0"