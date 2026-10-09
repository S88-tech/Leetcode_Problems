class Solution:
    def canThreePartsEqualSum(self, arr: list[int]) -> bool:
        total=sum(arr)
        if total%3!=0:
            return False
        # return True    
        target=total//3
        curr=parts=0
        for n in arr:
            curr+=n
            if curr==target:
                parts+=1
                curr=0
        return parts>=3        