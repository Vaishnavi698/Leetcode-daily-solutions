class SegmentTree:
    def __init__(self, n: int, MOD: int):
        self.n = n
        self.MOD = MOD
        self.sum1 = [0] * (4 * n)
        self.sum2 = [0] * (4 * n)
        self.lazy = [0] * (4 * n)

    def _apply(self, node: int, length: int, val: int):
        # sum2' = sum2 + 2*val*sum1 + val^2*length
        self.sum2[node] = (self.sum2[node] + 2 * val * self.sum1[node] + val * val * length) % self.MOD
        # sum1' = sum1 + val*length
        self.sum1[node] = (self.sum1[node] + val * length) % self.MOD
        self.lazy[node] = (self.lazy[node] + val) % self.MOD

    def _push(self, node: int, l: int, r: int):
        if self.lazy[node] != 0:
            mid = (l + r) // 2
            self._apply(2 * node, mid - l + 1, self.lazy[node])
            self._apply(2 * node + 1, r - mid, self.lazy[node])
            self.lazy[node] = 0

    def update(self, node: int, l: int, r: int, ql: int, qr: int, val: int):
        if ql <= l and r <= qr:
            self._apply(node, r - l + 1, val)
            return
        
        self._push(node, l, r)
        mid = (l + r) // 2
        if ql <= mid:
            self.update(2 * node, l, mid, ql, qr, val)
        if qr > mid:
            self.update(2 * node + 1, mid + 1, r, ql, qr, val)
        
        # FIXED: Correctly reference left child as (2 * node) instead of (node + 0)
        self.sum1[node] = (self.sum1[2 * node] + self.sum1[2 * node + 1]) % self.MOD
        self.sum2[node] = (self.sum2[2 * node] + self.sum2[2 * node + 1]) % self.MOD


from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        seg = SegmentTree(n, MOD)
        
        last_occurrence = {}
        total_ans = 0
        
        for j in range(n):
            x = nums[j]
            prev_idx = last_occurrence.get(x, -1)
            
            # Update range [prev_idx + 1, j] by +1
            seg.update(1, 0, n - 1, prev_idx + 1, j, 1)
            
            # Add the total sum of squares for all subarrays ending at j
            total_ans = (total_ans + seg.sum2[1]) % MOD
            
            last_occurrence[x] = j
            
        return total_ans