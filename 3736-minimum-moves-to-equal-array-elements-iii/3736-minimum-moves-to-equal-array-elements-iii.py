class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        maxi=max(nums)
        moves=0
        for x in nums:
            moves+=maxi-x
        return moves    
        