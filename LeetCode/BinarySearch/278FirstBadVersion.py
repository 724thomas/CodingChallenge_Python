#https://leetcode.com/problems/first-bad-version/
'''
1. 아이디어 :
    start, end로 두 포인터를 설정하고, isBadVersion(mid)를 통해 mid가 bad인지 아닌지 확인한다.
    확인 후, False면 start 포인터를, True면 end 포인터를 mid+-1로 옮긴다.
2. 시간복잡도 :
    1) O(logn)
3. 자료구조 :
    1) 배열
'''

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
class Solution:
    def firstBadVersion(self, n: int) -> int:
        start=0
        end=n
        mid=0
        while start<=end:
            mid=(start+end)//2
            check=isBadVersion(mid)
            if check:
                end=mid-1
            else:
                start=mid+1
        print(start,mid,end)
        return start