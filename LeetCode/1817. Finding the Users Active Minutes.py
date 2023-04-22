#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        ans=[0 for x in range(k)]
        act={x[0]:[] for x in logs}

        for user in logs:
            if user[1] not in act[user[0]]:
                act[user[0]].append(user[1])

        for k,v in act.items():
            if len(v)!=0:
                ans[len(v)-1]+=1
        return ans