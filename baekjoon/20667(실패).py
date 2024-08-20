# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''




import sys
#sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()

def solution(n, tCPU, tMEM, arr):
    dp = [[float('inf')] * (tCPU+1) for _ in range(tMEM+1)]
    dp[0][0] = 0
    arr.sort(key=lambda x: (-x[2]))

    for cpu, mem, priority in arr:
        for row in range(tMEM, mem-1, -1):
            for col in range(tCPU, cpu-1, -1):
                dp[row][col] = min(dp[row][col], dp[row-mem][col-cpu] + priority)
    print(*dp, sep='\n')

    return dp[tMEM][tCPU] if dp[tMEM][tCPU] != float('inf') else -1

def solution(n, tCPU, tMEM, arr):
    arr.sort(key=lambda x: x[2])
    ans = [float('inf')]
    def backtrack(idx, curr_c, curr_m, curr_p):
        if curr_c >= tCPU and curr_m >=tMEM:
            ans[0] = min(ans[0], curr_p)
            return

        if idx >= n or curr_p >= ans[0]:
            return
        cpu, mem, pri = arr[idx]

        backtrack(idx+1, curr_c + cpu, curr_m + mem, curr_p + pri)
        backtrack(idx+1, curr_c, curr_m, curr_p)

    backtrack(0,0,0,0)
    return ans[0] if ans[0] != float('inf') else -1

def solution(n, tCPU, tMEM, arr):
    max_priority = sum(pri for _, _, pri in arr)

    # DP 배열 초기화 (무한대 대신 음의 무한대로 초기화하여 최소화 문제에 맞게 설계)
    dp = [[-float('inf')] * (tCPU + 1) for _ in range(max_priority + 1)]
    dp[0][0] = 0  # 우선순위 0, CPU 0일 때 메모리 0으로 시작

    for cpu, mem, pri in arr:
        for p in range(max_priority - pri, -1, -1):
            for c in range(tCPU - cpu, -1, -1):
                if dp[p][c] != -float('inf'):
                    dp[p + pri][c + cpu] = max(dp[p + pri][c + cpu], dp[p][c] + mem)

    # 결과 계산: 최소 우선순위를 찾아서 반환
    for p in range(max_priority + 1):
        for c in range(tCPU + 1):
            if dp[p][c] >= tMEM:
                return p

    return -1

if __name__ == '__main__':
    n, m, k = map(int, input().split())
    arr = [list (map(int, input().split())) for _ in range(n)]
    print(solution(n, m, k, arr))

