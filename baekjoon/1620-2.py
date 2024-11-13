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

def solution(n, m):
    name_to_num = {}
    num_to_name = {}

    for i in range(n):
        pokemon = input()
        name_to_num[pokemon] = i+1
        num_to_name[i+1] = pokemon

    for i in range(m):
        query = input()
        if query[0].isnumeric():
            print(num_to_name[int(query)])
        else:
            print(name_to_num[query])

if __name__ == '__main__':
    n, m = map(int, input().split())
    solution(n, m)
