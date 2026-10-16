class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        sum_t = [0] * (4 * n)
        sq_t = [0] * (4 * n)
        lazy = [0] * (4 * n)
        
        def push(node, l, r):
            if lazy[node]:
                v = lazy[node]
                mid = (l + r) // 2
                for child, length in [(2 * node, mid - l + 1), (2 * node + 1, r - mid)]:
                    sq_t[child] = (sq_t[child] + 2 * v * sum_t[child] + v * v * length) % MOD
                    sum_t[child] = (sum_t[child] + v * length) % MOD
                    lazy[child] = (lazy[child] + v) % MOD
                lazy[node] = 0

        def update(node, l, r, ql, qr, val):
            if ql <= l and r <= qr:
                length = r - l + 1
                sq_t[node] = (sq_t[node] + 2 * val * sum_t[node] + val * val * length) % MOD
                sum_t[node] = (sum_t[node] + val * length) % MOD
                lazy[node] = (lazy[node] + val) % MOD
                return
            push(node, l, r)
            mid = (l + r) // 2
            if ql <= mid: update(2 * node, l, mid, ql, qr, val)
            if qr > mid: update(2 * node + 1, mid + 1, r, ql, qr, val)
            sum_t[node] = (sum_t[node] + sum_t[2 * node] + sum_t[2 * node + 1] - sum_t[node]) % MOD # safer update
            sum_t[node] = (sum_t[2 * node] + sum_t[2 * node + 1]) % MOD
            sq_t[node] = (sq_t[2 * node] + sq_t[2 * node + 1]) % MOD

        last = {}
        ans = 0
        current_sum_squares = 0
        
        for j, x in enumerate(nums):
            prev = last.get(x, -1)
            last[x] = j
            update(1, 0, n - 1, prev + 1, j, 1)
            ans = (ans + sq_t[1]) % MOD
            
        return ans