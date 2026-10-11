class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:

        n=len(arr)
        s=0
        for i in range(n):
            c=0
            for j in range(i,n):
                c+=arr[j]
                if (j-i+1)%2==1:
                    s+=c
        return s                       
                    
          

        