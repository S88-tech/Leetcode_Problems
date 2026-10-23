class Solution:
    def largestInteger(self, num: int) -> int:
        s = list(str(num))
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if int(s[i]) % 2 == int(s[j]) % 2 and s[i] < s[j]:
                    s[i], s[j] = s[j], s[i]
        return int(''.join(s))