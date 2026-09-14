class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        ans1 = strs[0]
        ans2 = strs[-1]
        c = 0
        while c < len(ans1) and c < len(ans2):
            if ans1[c] == ans2[c]:
                c += 1
            else:
                break
        return ans1[:c]
        