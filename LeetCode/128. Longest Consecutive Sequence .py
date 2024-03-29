# https://leetcode.com/problems/longest-consecutive-sequence/

'''
1. 아이디어 :
    nums를 해시셋으로 변환한다.
    각 숫자보다 1작은 숫자가 셋에 있으면 시작이 아니고,
    1작은 숫자가 없으면 시작이다.
    그 후로 숫자에 1씩 더하면서 해시셋에 존재하는지 확인하며 길이를 센다.
    길이의 최대값을 리턴
2. 시간복잡도 :
    O(n)
3. 자료구조 :
    해시셋
'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        cmax = 0

        for n in num_set:
            if (n-1) not in num_set:
                length = 0
                while (n+length) in num_set:
                    length+=1
                cmax = max(cmax, length)
        return cmax