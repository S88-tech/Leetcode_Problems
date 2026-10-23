class Solution:
    def sortEvenOdd(self, nums: list[int]) -> list[int]:
        ans=[]

        odd=sorted(nums[1::2],reverse=True)

        even=sorted(nums[::2])
        for i in range(len(nums)):
            if i%2==0:
                ans.append(even[i//2])
            else:
                ans.append(odd[i//2]) 
        return ans           
                          


        