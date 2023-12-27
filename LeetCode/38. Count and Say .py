# https://leetcode.com/problems/count-and-say/

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


class Solution:
    def countAndSay(self, n: int) -> str:

        def say(s):
            result = ""
            count = 1
            for i in range(len(s) - 1):
                if s[i] != s[i + 1]:
                    result += str(count) + s[i]
                    count = 1
                else:
                    count += 1

            return result + str(count) + s[-1]

        if n == 1:
            return "1"
        ans = "11"
        for i in range(n - 2):
            ans = say(ans)
        return ans
