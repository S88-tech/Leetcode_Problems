class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        arr=sorted(x**2 for x in nums)
        return arr
        