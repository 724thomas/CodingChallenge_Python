# https://www.acmicpc.net/problem/

'''
1. 아이디어 :
    조건들을 확인하고, 마지막에 백트래킹으로 확인한다.
2. 시간복잡도 :
    O(n)
3. 자료구조 :
    배열
'''

import sys

# sys.setrecursionlimit(1000000)
# input = sys.stdin.readline

input = lambda: sys.stdin.readline().rstrip()


def solution(arr):
    ans = []

    def is_possible(play):

        def backtrack(idx):
            if idx == len(match_results):
                return 1

            team1, team2 = match_results[idx]

            if wins[team1] > 0 and lose[team2] > 0:
                wins[team1] -= 1
                lose[team2] -= 1
                if backtrack(idx + 1):
                    return 1
                wins[team1] += 1
                lose[team2] += 1

            if draw[team1] > 0 and draw[team2] > 0:
                draw[team1] -= 1
                draw[team2] -= 1
                if backtrack(idx + 1):
                    return 1
                draw[team1] += 1
                draw[team2] += 1

            if lose[team1] > 0 and wins[team2] > 0:
                lose[team1] -= 1
                wins[team2] -= 1
                if backtrack(idx + 1):
                    return 1
                lose[team1] += 1
                wins[team2] += 1
            return 0

        wins, draw, lose = [0] * 6, [0] * 6, [0] * 6

        idx = 0
        for i in range(6):
            wins[i], draw[i], lose[i] = play[idx], play[idx + 1], play[idx + 2]
            idx += 3

        total_wins = sum(wins)
        total_lose = sum(lose)
        if total_wins != total_lose:  # 총 이긴횟수 - 총 진횟수 = 0
            return 0

        for i in range(6):  # 총 5 경기
            if wins[i] + draw[i] + lose[i] != 5:
                return 0

        total_draws = sum(draw)
        if total_draws % 2:  # 비긴 횟수가 홀수
            return 0
        for i in range(6):  # 비긴횟수 > 남은 비긴횟수
            if draw[i] > total_draws - draw[i]:
                return 0

        for i in range(6):
            if wins[i] > total_lose - lose[i]:
                return 0
            if lose[i] > total_wins - wins[i]:
                return 0

        match_results = [(i, j) for i in range(6) for j in range(i + 1, 6)]
        return backtrack(0)

    for p in arr:
        ans.append(is_possible(p))

    return ans


if __name__ == '__main__':
    arr = []
    for _ in range(4):
        arr.append(list(map(int, input().strip().split())))
    print(*solution(arr))
