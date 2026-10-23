class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        ans = [0]*len(nums)
        odd,even=1,0

        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                ans[even]=nums[i]
                even+=2

            else:
                ans[odd]=nums[i]
                odd+=2
        return ans        
