# https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/description/

'''
1. 아이디어 :
    카드 해시셋과 최소길이를 저장할 변수 cmin을 선언한다.
    카드를 순회하면서 카드가 해시셋에 있으면 cmin과 현재 인덱스 - 해시셋의 인덱스 + 1 중 최소값을 cmin에 저장한다.
    해시셋에 카드값을 추가하거나 수정한다..
2. 시간복잡도 :
    O(N)
3. 자료구조 :
    해시셋
'''


class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        card = {}
        cmin = float('inf')
        for i in range(len(cards)):
            if cards[i] in card:
                cmin = min(cmin,i - card[cards[i]] + 1)
            card[cards[i]] = i
        return -1 if cmin == float('inf') else cmin

