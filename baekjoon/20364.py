# https://www.acmicpc.net/problem/20364

'''
1. 아이디어 :
    각 병아리의 경로를 구하고, 해당 경로가 visited에 있는지 확인.
    있으면 해당 노드 값 출력하고 아니면 visited에 n을 넣는다.
2. 시간복잡도 :
    O( n * n )
3. 자료구조 :
    해시셋, 배열
'''


import sys
#sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def solution(n, q, wanted):

    def get_path(n):
        quack = n
        visited = []
        while n != 1:
            visited.append(n)
            n = n // 2

        for i in range(len(visited)-1, -1, -1):
            if visited[i] in visited_node:
                return visited[i]
        visited_node.add(quack)
        return 0

    visited_node = set()
    for quack in wanted:
        print(get_path(quack))


n, q = list(map(int, input().split()))
wanted = [int(input()) for _ in range(q)]
solution(n, q, wanted)


