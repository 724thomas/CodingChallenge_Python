#

'''
1. 아이디어 :
    백트래킹으로 풀 수 있다.
2. 시간복잡도 :
    O( 2 ^ n )
3. 자료구조 :
    스트링
'''


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(s, left, right):
            if left == right == 0:
                ans.append(s)
                return

            if left:
                backtrack(s+"(", left-1, right)

            if left < right:
                backtrack(s+")", left, right-1)

        backtrack("", n, n)
        return ans