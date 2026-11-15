class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10**9 + 7

        cum_sum = 0
        even_count = 1
        odd_count = 0
        res = 0

        for num in arr:
            cum_sum += num

            if cum_sum % 2 != 0:
                res += even_count
                odd_count += 1
            else:
                res += odd_count
                even_count += 1

            res %= MOD

        return res