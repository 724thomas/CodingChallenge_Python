#https://leetcode.com/problems/arranging-coins/description/


'''
1. 아이디어 :
    1) (967ms, 13.9MB)while문으로 sum, stair를 0으로 두고 sum < n일때까지 stair를 1씩 증가시키고, sum에 stair를 더한다.
    while문이 끝날때 sum이 n이면 stair를 리턴하고, 크면 stair-1을 리턴한다.
    2) (30ms, 13.8MB) 수학적으로 연산 할 수 있다.
    3) (40ms, 13.8MB) 이진탐색으로 값을 구할 수 있다.
2. 시간복잡도 :
    1) O(sqrt(n))
    -  while문을 sqrt(n)번 돌린다.
    2) O(1)
    3) O(logN)
    - 이진탐색
3. 자료구조 :
    1) X
    2) X
    3) Binary Search

'''
class Solution:
    def arrangeCoins1(self, n: int) -> int:
        stair=sum=0
        while sum<n:
            stair,sum =stair+1, sum+stair+1
        return stair-1 if sum!=n else stair

    def arrangeCoins2(self, n: int) -> int:
        return int((2*n+0.25)**0.5-0.5)

    def arrangeCoins3(self, n: int) -> int:
        start, end = 0,n
        while start<=end:
            mid = (start+end)//2
            if mid*(mid+1)//2 == n:
                return mid
            elif mid*(mid+1)//2 < n:
                start = mid+1
            elif mid*(mid+1)//2 > n:
                end = mid-1
        return end

