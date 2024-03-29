# https://leetcode.com/problems/implement-magic-dictionary/description/

'''
1. 아이디어 :
    길이가 같거나, 같은 단어가 아닐때 글자가 하나만 다른지 확인하면 된다.
2. 시간복잡도 :
    O(N * M)
    저장되는 단어의 수 * 각 단어와 검색하는 단어의 길이
3. 자료구조 :
    해시셋
'''


class MagicDictionary:

    def __init__(self):
        self.words = set()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.words.add(word)

    def search(self, searchWord: str) -> bool:
        for word in self.words:
            if len(word)==len(searchWord) and word!=searchWord:
                count = 0
                for i in range(len(word)):
                    if word[i] != searchWord[i]:
                        count += 1
                    if count >1:
                        break
                if count == 1:
                    return True
        return False



# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)