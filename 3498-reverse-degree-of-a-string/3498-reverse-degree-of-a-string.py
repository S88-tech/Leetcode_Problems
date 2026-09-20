class Solution:
    def reverseDegree(self, s: str) -> int:
        total=0
        for i in range(len(s)):
            a=ord("z")-ord(s[i])+1
            total+=a*(i+1)
        return total
        