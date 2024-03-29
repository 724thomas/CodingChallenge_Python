# https://leetcode.com/problems/array-partition/description/

'''
1. 아이디어 :
    - 정렬후, 짝수 인덱스에 있는 값들을 합한다.
2. 시간복잡도 :
    nlogn : 정렬(nlogn) + for문(n)
3. 자료구조 :
    리스트
'''


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum([nums[i] for i in range(0,len(nums),2)])