#

'''
1. 아이디어 :
    홀수가 나오는 index 저장.
    -1 와 마지막 len(num)은 인덱스 에러 방지
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    배열
'''


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odds = [-1]

        for i in range(len(nums)):
            if nums[i] % 2:
                odds.append(i)

        odds.append(len(nums))

        count = 0

        for i in range(1, len(odds) - k):
            left_even_count = odds[i] - odds[i-1]
            right_even_count = odds[i+k] - odds[i+k-1]
            count += left_even_count * right_even_count

        return count