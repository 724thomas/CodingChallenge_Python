# https://www.acmicpc.net/problem/5670

'''
1. 아이디어 :
    1) Trie를 이용하여 모든 단어를 저장하고, 저장된 단어를 하나씩 탐색하면서, 자식 노드가 1개인 경우에는
    자식 노드를 탐색하고, 자식 노드가 2개 이상인 경우에는 탐색을 중단하고, 탐색한 단어의 길이를
    저장한다.
2. 시간복잡도 :
    1) O(케이스) * O(단어의 개수) * O(단어의 길이) = O(케이스 * 단어의 개수 * 단어의 길이)
3. 자료구조 :
    1) Trie

'''

import sys

input = sys.stdin.readline


class TrieNode:
    def __init__(self,char):
        self.char=char
        self.children = {}
        self.endOfWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                temp = TrieNode(char)
                cur.children[char] = temp
                cur = temp
            else:
                cur = cur.children[char]
        cur.endOfWord = True

while True:
    TrieA = Trie()
    try:
        n = int(input())
    except:
        break
    words = []
    for _ in range(n):
        word = input().rstrip()
        words.append(word)
        TrieA.insert(word)

    ans = 0
    for word in words:
        temp = 0
        cur = TrieA.root
        for char in word:
            cur = cur.children[char]
            if len(cur.children) > 1 or cur.endOfWord:
                temp += 1
        ans += temp
    print("%.2f" % (ans / n))
