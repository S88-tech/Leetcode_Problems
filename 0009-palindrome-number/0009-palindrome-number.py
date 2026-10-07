class Solution:
    def isPalindrome(self, x: int) -> bool:
        p=str(x)[::-1]
        print(p)
        if x<0:
            return False
        return int(p)==x    
                 