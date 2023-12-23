#https://leetcode.com/problems/first-missing-positive/description/

'''
1. 아이디어 :
    - 새로운 배열을 만들지 않고, 기존 nums 배열에 존재하는지 저장하는 방식을 사용한다.
    - 첫번째 loop에서 0보다 작은 값들은 0으로 초기화를 시켜놓는다
    - 두번째 loop에서 val = nums[i]의 절대값이 정답의 최소, 최대 사이에 있는지 확인하고, val-1번째 인덱스가 0 이상이면, -로 바꿔서 존재한다고 체크한다.
    - val-1번째 인덱스가 0 일때는 -를 곱해도 0이기때문에, 답에 영향을 주지 않는 최대값*-1을 저장한다. (음수(=존재)라는걸 보여주기만 하면 된다)
    - 세번째 loop에서 정답의 최소 1부터 최대 nums의 길이+1까지 돌면서, nums[i-1]가 음수가 아닐때, 해당 i는 존재하지 않기때문에 i를 리턴
    - loop을 다 돌았을때는 len(nums)의 숫자까지 존재하기 때문에, len(nums)+1를 리턴
2. 시간복잡도 :
    O(n)
3. 자료구조 :
    배열
'''


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        for i in range(len(nums)):
            val = abs(nums[i])
            if 1 <= val <= len(nums):
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
                elif nums[val - 1] == 0:
                    nums[val - 1] = -1 * (len(nums) + 1)

        for i in range(1, len(nums) + 1):
            if nums[i - 1] >= 0:
                return i

        return len(nums) + 1

        '''
        O(n), O(n)
        nums = set(nums)
        for i in range(1, len(nums)+1):
            if i not in nums:
                return i
        '''
