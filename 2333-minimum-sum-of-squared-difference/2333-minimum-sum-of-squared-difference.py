
class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        k = k1 + k2
        arr = []

        for i in range(len(nums1)):
            arr.append(abs(nums1[i] - nums2[i]))

        if sum(arr) <= k:
            return 0

        low = 0
        high = max(arr)

        while low < high:
            mid = (low + high) // 2
            count = 0

            for num in arr:
                if num > mid:
                    count += num - mid

            if count <= k:
                high = mid
            else:
                low = mid + 1

        count = 0
        ans = 0

        for num in arr:
            if num > low:
                count += num - low
                ans += low ** 2
            else:
                ans += num ** 2

        rem = k - count

        for num in arr:
            if rem > 0 and num >= low:
                ans -= low ** 2
                ans += (low - 1) ** 2
                rem -= 1

        return ans
