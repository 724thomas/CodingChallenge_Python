# https://www.acmicpc.net/problem/1422

'''
1. 아이디어 :
    자릿수가 가장 많은 숫자들 중, 두개씩(a, b)를 비교해서 더 큰 값을 arr에 추가한다.
    arr의 길이만큼 반복해서, arr[i]와 arr[i+1]의 크기를 비교해서 더 큰걸 앞에다 둔다. (정렬)
2. 시간복잡도 :
    O( n^2 )
3. 자료구조 :
    배열
'''

import sys

# sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(n, k, arr):
    def compare(a, b):
        return int(a + b) >= int(b + a)

    arr.sort(key=lambda x: len(x), reverse=True)
    candids = [arr[0]]
    for i in range(1, len(arr)):
        if len(arr[i]) == len(arr[0]):
            candids.append(arr[i])
    candid = candids[0]
    for i in range(1, len(candids)):
        if not compare(candid, candids[i]):
            candid = candids[i]

    for _ in range(k - len(arr)):
        arr.append(candid)
    for _ in range(len(arr)):
        for i in range(len(arr) - 1):
            if not compare(arr[i], arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return int("".join(arr))


n, k = list(map(int, input().split()))
arr = []
for _ in range(n):
    arr.append(str(input().strip()))
print(solution(n, k, arr))
