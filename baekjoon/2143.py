# https://www.acmicpc.net/problem/2143

'''
1. 아이디어 :
    get_subarray_sums를 백트래킹으로 했을때 recursion이 생기므로 이중 루프로 풀었다
2. 시간복잡도 :
    O( n**2 )
3. 자료구조 :
    해시맵
'''


import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

from collections import defaultdict
def solution(target, arr1, arr2):

    def get_subarray_sums(arr):
        subarray_sums = defaultdict(int)
        n = len(arr)
        for i in range(n):
            total = 0
            for j in range(i, n):
                total += arr[j]
                subarray_sums[total] += 1
        return subarray_sums

    map1 = get_subarray_sums(arr1)
    map2 = get_subarray_sums(arr2)

    ans = 0
    for k,v in map1.items():
        temp = target - k
        if temp in map2:
            ans += (v * map2[temp])
    return ans


target= int(input())
input()
arr1 = list(map(int, input().strip().split()))
input()
arr2 = list(map(int, input().strip().split()))
print(solution(target, arr1, arr2))


