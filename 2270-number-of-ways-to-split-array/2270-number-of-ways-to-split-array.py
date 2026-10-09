class Solution:
    def waysToSplitArray(self, nums: list[int]) -> int:
        left=0
        n=len(nums)
        total=sum(nums)
        count=0
        for i in range(len(nums)-1):
            left+=nums[i]
            right=total-left
            if right<=left:
                count=count+1
            
        return count

        