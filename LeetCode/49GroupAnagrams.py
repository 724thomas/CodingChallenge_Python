#https://leetcode.com/problems/group-anagrams/description/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alist=[]
        ans=[]
        check=[1 for x in range(len(strs))]
        strsSort = [sorted(x) for x in strs]
        print(check)
        for i in range(len(strs)):
            tempans=[strs[i]]
            if strsSort[i] not in alist:
                alist.append(strsSort[i])
            else:
                continue
            for j in range(i+1,len(strs)):
                if check[j]==0:
                    continue
                if strsSort[i]==strsSort[j]:
                    check[j]=0
                    tempans.append(strs[j])
            ans.append(tempans)
        return ans