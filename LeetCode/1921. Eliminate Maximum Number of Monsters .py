# https://leetcode.com/problems/eliminate-maximum-number-of-monsters/description/

'''
1. 아이디어 :
    각 몬스터가 도착하는데 얼마나 걸리는지 게산한 minites 배열을 만든다.
    첫발은 장전 되있으므로, kill은 1부터 시작하고, minites도 가장 빠르게 도착할 몬스터를 제외한다.
    for문을 돌면서 minites[i] - kill 이 >0 넘으면 죽일 수 있고, 없으면 죽일 수 없으므로 kills를 리턴한다.
2. 시간복잡도 :
    O(nLogn)
3. 자료구조 :
    배열
'''

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        minites = sorted([dist[i]/speed[i] for i in range(len(dist))])[1:]
        kills = 1

        for i in range(len(minites)):
            if minites[i] - kills >0:
                kills+=1
            else:
                break
        return kills