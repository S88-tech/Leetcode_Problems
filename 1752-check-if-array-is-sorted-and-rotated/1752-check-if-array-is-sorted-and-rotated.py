class Solution:
    def check(self, nums: list[int]) -> bool:
        for i in range(len(nums)):
            rotated=nums[i:]+nums[:i]  
            if rotated==sorted(nums):
                return True
        return False        

        
        