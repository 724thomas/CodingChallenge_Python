# https://leetcode.com/problems/find-the-duplicate-number/description/

'''
1. 아이디어 :
    기존 배열에 존재하는지 체크하는 방식을 사용
    nums[i]의 절대값-1번쨰 인덱스가 0보다 크면, -로 바꿔서 존재한다고 체크한다.
    0보다 작으면 이미 체크했기때문에 중복된 숫자이다.
2. 시간복잡도 :
    O(n)
3. 자료구조 :
    배열
'''


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            val = abs(nums[i])
            if nums[val - 1] >= 0:
                nums[val - 1] *= -1
            else:
                return abs(nums[i])
