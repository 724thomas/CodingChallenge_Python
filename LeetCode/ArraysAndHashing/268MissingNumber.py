# https://leetcode.com/problems/missing-number/
'''
1. 아이디어 :
    1) 정렬 시킨 후, while문안에 start<=end 투 포인터로 해당값이랑 인덱스랑 일치하는지 확인한다. 맞을 시 답은 오른쪽에 위치,
    반댈로 틀릴 시 답은 왼쪽에 위치. start를 반환
2. 시간복잡도 :
    1) O(logn) + O(n) = O(n)
    - sort * 2중포문 * 투포인터
3. 자료구조 :
    1) 배열

'''

class Solution:
    def missingNumber(self, n: List[int]) -> int:
        n.sort()
        start=0
        end=len(n)-1
        while start<=end:
            mid=(start+end)//2
            if mid==n[mid]:
                start=mid+1
            elif mid!=n[mid]:
                end=mid-1
        return start