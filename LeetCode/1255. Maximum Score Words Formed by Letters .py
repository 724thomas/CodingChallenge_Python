# https://leetcode.com/problems/maximum-score-words-formed-by-letters/description/

'''
1. 아이디어 :
    백트래킹을 사용.
    words를 Counter로 변환하고, counter로 만든 letter를 뺐을때, 값이 없으면(FALSE)로 백트래킹을 종료한다.
    그게 아니면 Counter로 총 letters를 구하고, words를 Counter로 만들어서 빼준다.
2. 시간복잡도 :
    O(n**2)
3. 자료구조 :
    배열
'''

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        score = [sum(score[ord(c)-ord('a')] for c in w) for w in words]
        words = list(map(Counter, words))

        res = [0]
        def dfs(i, cur, c):
            res[0] = max(res[0], cur)
            for j, w in enumerate(words[i:], i):
                if not w - c:
                    dfs(j+1, cur + score[j], c - w)


        dfs(0, 0, Counter(letters))
        return res[0]