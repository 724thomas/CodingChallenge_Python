# https://www.acmicpc.net/problem/15665

'''
1. 아이디어 :
    1) 백트래킹/dsf로 풀 수 있을거 같다
    2) itertools의 product로 풀 수 있다
2. 시간복잡도 :
    1) O(N*logN) + O(N^M) = O(N*logN + N^M)
        정렬 + N개의 숫자에 대해 M번 호출
    2) O(N^M)
        itertools.product 연산이지만 1번이 더 빠르다?
3. 자료구조 :
    1) 배열, 해시셋(중복제거)
    2) 배열, 헤시셋
'''

#1)
import sys
input = sys.stdin.readline
n, m = map(int,input().split())
nums = sorted(list(set(map(int,input().split()))))

temp=[]
def backtracking():
    if len(temp) == m: #추가된 숫자의 갯수가 m개일때
        print(*temp) #temp 배열안에 모든 숫자를 한줄에 출력
        return

    for i in range(len(nums)):
        temp.append(nums[i]) #temp에 num[i]를 추가
        backtracking() #추가된 temp를 가지고 다시 연산시작
        temp.pop() #temp에 num[i]를 제거

backtracking()

#2)
import sys
from itertools import product

input = sys.stdin.readline

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

result = set(product(nums, repeat=m))
output = []
for combination in sorted(result):
    print(*combination)