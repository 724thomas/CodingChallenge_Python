#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ans = set()

        for email in emails:
            domain = email.split("@")[1]
            url = ""
            for c in email:
                if c==".":
                    continue
                if c=="+" or c=="@":
                    break
                url+=c
            ans.add(url+"@"+domain)
        return len(ans)