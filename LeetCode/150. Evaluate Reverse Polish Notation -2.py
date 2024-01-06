#https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        print(-6//132)
        alist=[]
        for i in tokens:
            if i not in "+-*/":
                alist.append(int(i))
            else:
                temp1=alist.pop()
                temp2=alist.pop()
                if i=="+":
                    temp=temp2+temp1
                elif i=="-":
                    temp=temp2-temp1
                elif i=="*":
                    temp=temp2*temp1
                else:
                    temp=temp2/temp1
                    if temp<0:
                        temp=(-temp2//temp1)*-1
                    else:
                        temp=temp2//temp1
                alist.append(temp)
                print( str(temp2) + i + str(temp1) + "=" + str(temp) )
        return alist[0]