#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        n = len(word)
        ans = set()
        def backtrack(idx, s):
            if idx >= n:
                ans.add(s)
                return

            backtrack(idx+1, s+word[idx])
            if not s[-1].isnumeric():
                for size in range(1, n-idx+1):
                    backtrack(idx+size, s+str(size))

        backtrack(1, word[0])
        for i in range(1, n+1):
            backtrack(i, str(i))


        return ans