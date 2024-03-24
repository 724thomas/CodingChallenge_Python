#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''


from collections import defaultdict
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        memo = {"0": [1, 0], "1": [0, 1]}

        def dfs(s):
            if s == "0":
                return [1,0]
            if s == "1":
                return [0,1]
            if s in memo:
                return memo[s]

            zo = dfs(s[1:]).copy()
            if s[0] == "0":
                zo[0] +=1
            elif s[0] == "1":
                zo[1] +=1
            memo[s] = zo.copy()
            return zo

        for s in strs:
            dfs(s)


        dp = {}
        def dfs(idx, zeros, ones):
            if idx == len(strs):
                return 0
            if (idx, zeros, ones) in dp:
                return dp[(idx ,zeros,ones)]
            zero, one = memo[strs[idx]]

            dp[(idx, zeros, ones)] = dfs(idx+1, zeros, ones)

            if zero <= zeros and one <= ones:
                dp[(idx, zeros, ones)] = max(
                    dp[(idx, zeros, ones)],
                    1 + dfs(idx+1, zeros-zero, ones-one)
                )

            return dp[(idx,zeros,ones)]

        return dfs(0,m,n)