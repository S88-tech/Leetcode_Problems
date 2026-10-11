class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max1=0
        l=0
        seen=set()
        for r,c in enumerate(s):
            while  c in seen:
                seen.remove(s[l])
                l+=1 
            seen.add(c)
            max1=max(max1,r-l+1) 
        return max1          

        