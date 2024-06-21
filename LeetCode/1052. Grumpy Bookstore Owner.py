#

'''
1. 아이디어 :
    슬라이딩 윈도우
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    베얄
'''


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        total = sum([customers[i] for i in range(len(customers)) if not grumpy[i]])
        total += sum([customers[i] for i in range(minutes) if grumpy[i]])

        ans, left, right = total, 0, minutes

        while right < len(customers):
            total -= customers[left] if grumpy[left] else 0
            total += customers[right] if grumpy[right] else 0
            left, right, ans = left+1, right+1, max(ans, total)
        return ans

