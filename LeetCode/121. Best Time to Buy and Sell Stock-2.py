#

'''
1. 아이디어 :
    cmax를 움직이면서, cmin보다 작아지면 cmin을 갱신한다.
    cmax-cmin을 계산하며 최대값을 갱신한다.
2. 시간복잡도 :
    O( n )
3. 자료구조 :
ㅤㅤ
'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        cmin = 0
        for cmax in range(1, len(prices)):
            if prices[cmin] < prices[cmax]:
                ans = max(ans, prices[cmax]-prices[cmin])
            else:
                cmin = cmax
        return ans

