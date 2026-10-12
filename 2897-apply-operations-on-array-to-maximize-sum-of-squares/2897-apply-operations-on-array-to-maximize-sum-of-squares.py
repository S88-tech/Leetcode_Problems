class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        bit_counts = [0] * 32
        for x in nums:
            for i in range(32):
                if (x >> i) & 1:
                    bit_counts[i] += 1          
    
        max_nums = [0] * len(nums)
        for i in range(32):
            for j in range(bit_counts[i]):
                max_nums[j] |= (1 << i)
                
        total_sum = 0
        for i in range(k):
            total_sum = (total_sum + max_nums[i] * max_nums[i]) % MOD
            
        (total_sum)
        return total_sum
        