class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        n1=len(str(n))
        ans=[]
        place=1
        while n>0:
            r=n%10
            if r!=0:
                ans.append(r*place)
            n//=10
            place=place*10
        return ans[::-1]        

        