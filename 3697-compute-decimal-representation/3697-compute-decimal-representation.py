class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        ans = []
        for i, d in enumerate(str(n)[::-1]):
            if d != '0':
                ans.append(int(d) * (10 ** i))
        return ans[::-1]    

        