class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key=lambda x:x*x)
        n=len(nums)
        total=0
        for i in range(len(nums)):
            if i<n//2:
                total-=nums[i]*nums[i]
            else:
                total+=nums[i]*nums[i]
        return total        

        