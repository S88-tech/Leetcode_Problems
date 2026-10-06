class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # p=math.prod(nums)
        # ans=[]
        # for x in nums:
        #     if x>0:
        #         ans.append(p//x)
        # print(ans)
        # return 
        ans=[1]*len(nums)
        prefix=1
        for i in range(len(nums)):
            ans[i]=prefix
            prefix*=nums[i]
        suffix=1    
        for i in range(len(nums)-1,-1,-1):
            ans[i]*=suffix
            suffix*=nums[i]
        return ans    



            