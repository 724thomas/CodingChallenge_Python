#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


class Solution:
    def allPathsSourceTarget(self, g: List[List[int]]) -> List[List[int]]:
        ans=[]
        path=[0]
        def dfs(nums):
            if not nums:
                return
            for num in nums:
                path.append(num)
                if num==len(g)-1:
                    ans.append(path.copy())
                dfs(g[num])
                path.pop()

        dfs(g[0])
        return ans

