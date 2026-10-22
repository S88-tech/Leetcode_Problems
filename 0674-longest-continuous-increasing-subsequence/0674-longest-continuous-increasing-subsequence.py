class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        n=len(nums)
        ans=1
        c=1
        for i in range(1,n):
            if nums[i]>nums[i-1]:
                c+=1
            else:
                c=1
            ans=max(ans,c)

        return ans                    


        

        