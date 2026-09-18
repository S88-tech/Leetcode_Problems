class Solution:
    def findGCD(self, nums: list[int]) -> int:
        small=min(nums)
        print(small)
        biggest=max(nums)
        print(biggest)
        if biggest%small==0:
            return small
        return math.gcd(small,biggest)   
        