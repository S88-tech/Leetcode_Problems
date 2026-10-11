class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n=len(nums)
        ans=[]
        for i in range(n):
            ans.append(nums[i]*nums[i])
        print(ans) 
        sum=0 
        for i in range(len(nums)):
            if n%(i+1)==0:
                sum+=ans[i]
        return sum       



        