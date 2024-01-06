# https://leetcode.com/problems/word-ladder/description/

'''
1. 아이디어 :
    기존 bfs로 풀게되면 시간이 오래걸린다.
    n이 최대 5000, m이 최대 10이기때문에 O(n^2 * m)
    그래프를 먼저 만들어서 시간을 줄인다 O(n * m^2)
2. 시간복잡도 :
    O(n * m^2)
3. 자료구조 :
    해시맵
'''

from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        l = len(beginWord)
        all_combinations = defaultdict(list)
        for word in wordList:
            for i in range(l):
                key = word[:i] + "*" + word[i+1:]
                all_combinations[key].append(word)

        def find_words(word):
            candids = []
            for i in range(l):
                key = word[:i] + "*" + word[i+1:]
                for words in all_combinations[key]:
                    if words not in visited:
                        candids.append(words)
            return candids

        queue = deque()
        queue.append((beginWord,1))
        visited = set()
        visited.add(beginWord)
        while queue:
            word, count = queue.popleft()
            if word == endWord:
                return count
            candid_words = find_words(word)
            for w in candid_words:
                visited.add(w)
                queue.append((w,count+1))
        return 0




#시간초과
'''
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList or beginWord == endWord:
            return 0
        visited = set()
        visited.add(beginWord)
        words = deque()
        words.append((beginWord,1))

        def possible(word1, word2):
            changed = False
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    if changed:
                        return False
                    changed=True
            return changed

        while words:
            word, count = words.popleft()
            if word == endWord:
                return count

            for change_word in wordList:
                if possible(word, change_word) and change_word not in visited:
                    visited.add(change_word)
                    words.append((change_word, count+1))

        return 0
'''
