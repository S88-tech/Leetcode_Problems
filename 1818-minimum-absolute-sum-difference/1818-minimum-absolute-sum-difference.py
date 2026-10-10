
class Solution:
    def minAbsoluteSumDiff(self, nums1: list[int], nums2: list[int]) -> int:
        mod = 10**9 + 7
        arr = sorted(nums1)

        total = 0
        best = 0

        for i in range(len(nums1)):
            diff = abs(nums1[i] - nums2[i])
            total += diff

            left = 0
            right = len(arr) - 1

            while left <= right:
                mid = (left + right) // 2

                if arr[mid] == nums2[i]:
                    left = mid
                    break
                elif arr[mid] < nums2[i]:
                    left = mid + 1
                else:
                    right = mid - 1

            if left < len(arr):
                new_diff = abs(arr[left] - nums2[i])
                best = max(best, diff - new_diff)

            if right >= 0:
                new_diff = abs(arr[right] - nums2[i])
                best = max(best, diff - new_diff)

        return (total - best) % mod
