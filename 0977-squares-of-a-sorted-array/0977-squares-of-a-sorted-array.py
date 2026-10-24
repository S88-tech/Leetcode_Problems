class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        ans=[]
        for x in nums:
            ans.append(x**2)
        ans.sort()  
        return ans  

        