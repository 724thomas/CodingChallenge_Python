#https://leetcode.com/problems/latest-time-by-replacing-hidden-digits/

class Solution:
    def maximumTime(self, time: str) -> str:
        ans=""
        #hour
        if time[0:2]=="??":
            ans+="23"
        elif time[0]=="?":
            if int(time[1])<4:
                ans+="2" + time[1]
            else:
                ans+="1" + time[1]
        elif time[1]=="?":
            if int(time[0])<2:
                ans+=time[0]+ "9"
            else:
                ans+=time[0] + "3"
        else:
            ans+=time[0:2]
        ans+=":"
        #minite
        if time[3:5]=="??":
            ans+="59"
        elif time[3]=="?":
            ans+="5" + time[4]
        elif time[4]=="?":
            ans+=time[3] + "9"
        else:
            ans+=time[3:5]
        return ans
