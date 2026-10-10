class Solution:
    def minDifference(self, nums: list[int]) -> int:
        maxDiff = 0
        mn = 10**9
        mx = 0
        for i in range(1, len(nums)):
            if (nums[i - 1] == -1) != (nums[i] == -1):
                val = max(nums[i - 1], nums[i])
                mn = min(mn, val)
                mx = max(mx, val)
            else:
                maxDiff = max(maxDiff, abs(nums[i - 1] - nums[i]))

        low = maxDiff
        high = (mx - mn + 1) // 2

        while low < high:
            mid = (low + high) // 2

            if self.check(nums, mid, mn + mid, mx - mid):
                high = mid
            else:
                low = mid + 1

        return low

    def check(self, nums, d, x, y):
        prev = 0
        count = 0
        for num in nums:
            if num == -1:
                count += 1
                continue
            if prev > 0 and count > 0:
                if count == 1:
                    a = min(max(abs(prev - x), abs(num - x)),
                            max(abs(prev - y), abs(num - y)))
                    if a > d:
                        return False
                else:
                    ax = abs(prev - x)
                    ay = abs(prev - y)
                    bx = abs(num - x)
                    by = abs(num - y)
                    xy = abs(x - y)

                    a = min(
                        max(ax, bx),
                        max(ay, by),
                        max(ax, xy, by),
                        max(ay, xy, bx)
                    )

                    if a > d:
                        return False

            prev = num
            count = 0

        if nums[0] == -1:
            for num in nums:
                if num != -1:
                    if min(abs(num - x), abs(num - y)) > d:
                        return False
                    break
        if nums[-1] == -1:
            for num in reversed(nums):
                if num != -1:
                    if min(abs(num - x), abs(num - y)) > d:
                        return False
                    break
        return True