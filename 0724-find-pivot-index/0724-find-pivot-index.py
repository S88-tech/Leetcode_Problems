class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left=0
        n=len(nums)
        for i in range(len(nums)):
            right=sum(nums)-left-nums[i]
            if right==left:
                return i
            left+=nums[i]
        return -1          