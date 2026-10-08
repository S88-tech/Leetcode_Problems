class Solution:
    def countValidWords(self, s: str) -> int:
        return sum(
            1 for w in s.split()
            if not any(c.isdigit() for c in w)
            and w.count('-') <= 1
            and w.count('!') + w.count('.') + w.count(',') <= (1 if w[-1] in '!.,' else w.count('!') + w.count('.') + w.count(',') == 0)
            and not w.startswith('-') and not w.endswith('-')
            and all(w[i-1].islower() and w[i+1].islower() for i, c in enumerate(w) if c == '-')
            and all(c not in '!.,' or i == len(w) - 1 for i, c in enumerate(w))
        )
        