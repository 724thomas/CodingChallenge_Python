#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        travel=[0]+travel
        mg=mp=mm=0
        cg=cp=cm=0
        for i in range(len(travel)-1):
            travel[i+1]+=travel[i]
        for i in range(len(garbage)):
            if "M" in garbage[i]:
                mm=travel[i]
                cm+=garbage[i].count("M")
            if "P" in garbage[i]:
                mp=travel[i]
                cp+=garbage[i].count("P")
            if "G" in garbage[i]:
                mg=travel[i]
                cg+=garbage[i].count("G")

        return mm+cm+mp+cp+mg+cg