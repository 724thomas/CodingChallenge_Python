#

'''
1. 아이디어 :
    encodeUrl에 저장되어 있는 개수만큼 tinyurl을 생성하고, decodeUrl에 저장되어 있는 개수만큼 longUrl을 생성한다.
2. 시간복잡도 :
    O( 1 )
3. 자료구조 :

'''

class Codec:
    def __init__(self):
        self.encodeUrl = {}
        self.decodeUrl = {}
        self.base = "https://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        if longUrl not in self.encodeUrl:
            tinyurl = self.base + str(len(self.encodeUrl)+1)
            self.encodeUrl[longUrl] = tinyurl
            self.decodeUrl[tinyurl] = longUrl
        return self.encodeUrl[longUrl]

    def decode(self, shortUrl: str) -> str:
        return self.decodeUrl[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))