#https://leetcode.com/problems/minimum-health-to-beat-game/

'''
1. 아이디어 :
    최대로 받을 수 있는 데미지를 구하고 그것을 뺀다.
2. 시간복잡도 :
    O(n)
3. 자료구조 :
    리스트
'''


class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        cmax=0
        total=0
        for d in damage:
            total+=d
            cmax=max(cmax,d)
        cmax=min(armor,cmax)
        return total-cmax+1