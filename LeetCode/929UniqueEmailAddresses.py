#https://leetcode.com/problems/unique-email-addresses/description/

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ans=[]
        for i in range(len(emails)):
            ldName = emails[i].split("@")
            domainName= ldName[1]
            localName = ldName[0][:ldName[0].index("+")] if "+" in ldName[0] else ldName[0]
            localName=localName.replace(".","")
            totalName=localName+"@"+domainName
            if totalName not in ans:
                ans.append(totalName)
        return len(ans)