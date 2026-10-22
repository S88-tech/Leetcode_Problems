class Solution:
    def maxPower(self, s: str) -> int:
        if not s:
            return 0
        n=len(s)
        ans=1
        c=1
        for i in range(1,n):
            if s[i]==s[i-1]:
                c+=1
            else:
                c=1
            ans=max(ans,c)  
        return ans      

        