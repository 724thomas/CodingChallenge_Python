# https://leetcode.com/problems/encode-and-decode-strings/description/

'''
1. 아이디어 :

2. 시간복잡도 :
    O( n )
3. 자료구조 :

'''

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return "가".join(strs)


    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        return s.split("가")



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))