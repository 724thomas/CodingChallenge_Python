# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 / 알고리즘 :

'''


import sys
from collections import Counter

input = lambda: sys.stdin.readline().rstrip()

def is_similar(base, word):
    base_count = Counter(base)
    word_count = Counter(word)

    diff = 0
    for c in set(base_count.keys()) | set(word_count.keys()):
        diff += abs(base_count[c] - word_count[c])

    length_diff = abs(len(base) - len(word))

    if diff == 0:
        return True
    if diff == 1 and length_diff == 1:
        return True
    if diff == 2 and length_diff == 0:
        return True
    return False

def solution(n, base, arr):
    ans = 0
    for word in arr:
        if is_similar(base, word):
            ans += 1
    return ans

if __name__ == '__main__':
    n = int(input())
    base = input()
    arr = [input() for _ in range(n - 1)]
    print(solution(n, base, arr))

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