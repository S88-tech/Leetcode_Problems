class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum < 0 or sum > num * 9:
            return ""
        
        result = []
        for i in range(num):
            curr = min(9, sum)
            result.append(str(curr))
            sum -= curr
            
        return "".join(result)
        