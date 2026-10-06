class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = math.prod(nums)
        zeros = nums.count(0)
        ans = []

        for x in nums:
            if zeros > 1:
                ans.append(0)

            elif zeros == 1:
                if x == 0:
                    q = 1
                    for n in nums:
                        if n != 0:
                            q *= n
                    ans.append(q)
                else:
                    ans.append(0)

            else:
                ans.append(p // x)

        return ans