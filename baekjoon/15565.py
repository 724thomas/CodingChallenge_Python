# https://www.acmicpc.net/problem/15565

'''
1. 아이디어 :
    1의 인덱스만 저장을 한다.
    i와 k-i-1 인덱스에 있는 값이 길이가 된다.
    ones 배열의 ones길이-k-1까지 min을 구한다.
2. 시간복잡도 :
    O(n)
3. 자료구조 :
    배열
'''

n, k = map(int,input().split())
nums = list(map(int, input().split()))
ones = []
for i in range(len(nums)):
    if nums[i] == 1:
        ones.append(i)
if len(ones) < k:
    print(-1)
elif len(ones) == k:
    print(k)
else:
    cmin = float('inf')
    for i in range(len(ones)-k+1):
        cmin = min(cmin, ones[k+i-1] - ones[i] + 1)
    print(cmin)