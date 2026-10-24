class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        return sorted(map(lambda x:x**2,nums))

        