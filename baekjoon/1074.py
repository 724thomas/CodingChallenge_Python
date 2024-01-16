# https://www.acmicpc.net/problem/1074 Z

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''

def solution(n, r, c):

    def dfs(size, x, y, r, c):
        if size == 1:
            return 0
        size //= 2
        if r < x + size and c < y + size:  # 왼쪽 상단
            return dfs(size, x, y, r, c)
        elif r < x + size and c >= y + size:  # 오른쪽 상단
            return size * size + dfs(size, x, y + size, r, c)
        elif r >= x + size and c < y + size:  # 왼쪽 하단
            return 2 * size * size + dfs(size, x + size, y, r, c)
        else:  # 오른쪽 하단
            return 3 * size * size + dfs(size, x + size, y + size, r, c)

    return dfs(n, 0, 0, r, c)

n, r, c = map(int, input().split())
print(solution(2 ** n, r, c))