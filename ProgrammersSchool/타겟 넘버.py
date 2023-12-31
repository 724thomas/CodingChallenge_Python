# https://school.programmers.co.kr/learn/courses/30/lessons/43165 타겟넘버

'''
1. 아이디어 :
    dfs로 +일때, -일때 모두 구한다.
2. 시간복잡도 :
    2^n
3. 자료구조 :
    배열
'''


def solution(numbers, target):
    def dfs(idx, total):
        if idx == len(numbers):
            if total == target:
                ans[0] += 1
            return

        dfs(idx + 1, total + numbers[idx])
        dfs(idx + 1, total - numbers[idx])

    ans = [0]
    dfs(0, 0)
    return ans[0]
