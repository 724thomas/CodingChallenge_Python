#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


class Trie():
    def __init__(self):
        self.children = {}
        self.end = False

    def add_word(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = Trie()
            curr = curr.children[c]
        curr.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        def dfs(row1, col1, node, word):
            if not (0<=row1<len(board) and 0<=col1<len(board[0])):
                return
            if board[row1][col1] not in node.children or (row1,col1) in visited:
                return

            visited.add((row1,col1))
            node = node.children[board[row1][col1]]
            word += board[row1][col1]
            if node.end:
                ans.add(word)

            for row2, col2 in dir:
                nrow, ncol = row1 + row2, col1+ col2
                dfs(nrow, ncol, node, word)
            visited.remove((row1, col1))

        ans, visited = set(), set()
        dir = [[0,1], [0,-1], [-1,0], [1,0]]
        trie_root = Trie()
        for word in words:
            trie_root.add_word(word)

        for row in range(len(board)):
            for col in range(len(board[0])):
                dfs(row, col, trie_root, "")

        return list(ans)



