from typing import List

class SegmentTree:
    def __init__(self, nums: List[int], k: int):
        self.n = len(nums)
        self.k = k
        self.tree_prod = [1] * (4 * self.n)
        self.tree_counts = [[0] * k for _ in range(4 * self.n)]
        self.build(nums, 0, 0, self.n - 1)

    def _merge(self, node: int, left_child: int, right_child: int):
        self.tree_prod[node] = (self.tree_prod[left_child] * self.tree_prod[right_child]) % self.k
        
        # Reset current node counts
        for r in range(self.k):
            self.tree_counts[node][r] = self.tree_counts[left_child][r]
            
        left_p = self.tree_prod[left_child]
        for r in range(self.k):
            cnt = self.tree_counts[right_child][r]
            if cnt > 0:
                new_mod = (left_p * r) % self.k
                self.tree_counts[node][new_mod] += cnt

    def build(self, nums: List[int], node: int, l: int, r: int):
        if l == r:
            val_mod = nums[l] % self.k
            self.tree_prod[node] = val_mod
            self.tree_counts[node][val_mod] = 1
            return

        mid = (l + r) // 2
        self.build(nums, 2 * node + 1, l, mid)
        self.build(nums, 2 * node + 2, mid + 1, r)
        self._merge(node, 2 * node + 1, 2 * node + 2)

    def update(self, node: int, l: int, r: int, idx: int, val: int):
        if l == r:
            val_mod = val % self.k
            self.tree_prod[node] = val_mod
            self.tree_counts[node] = [0] * self.k
            self.tree_counts[node][val_mod] = 1
            return

        mid = (l + r) // 2
        if idx <= mid:
            self.update(2 * node + 1, l, mid, idx, val)
        else:
            self.update(2 * node + 2, mid + 1, r, idx, val)
        self._merge(node, 2 * node + 1, 2 * node + 2)

    def query(self, node: int, l: int, r: int, ql: int, qr: int):
        # Returns tuple: (product_mod_k, counts_array)
        if ql <= l and r <= qr:
            return self.tree_prod[node], self.tree_counts[node]

        mid = (l + r) // 2
        if qr <= mid:
            return self.query(2 * node + 1, l, mid, ql, qr)
        if ql > mid:
            return self.query(2 * node + 2, mid + 1, r, ql, qr)

        left_p, left_c = self.query(2 * node + 1, l, mid, ql, qr)
        right_p, right_c = self.query(2 * node + 2, mid + 1, r, ql, qr)

        res_p = (left_p * right_p) % self.k
        res_c = list(left_c)
        for rem in range(self.k):
            if right_c[rem] > 0:
                new_mod = (left_p * rem) % self.k
                res_c[new_mod] += right_c[rem]

        return res_p, res_c


class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        st = SegmentTree(nums, k)
        ans = []

        for idx, val, start, target_x in queries:
            # 1. Update nums[idx] persistently
            st.update(0, 0, n - 1, idx, val)
            
            # 2. Query range [start, n - 1] for target_x
            _, counts = st.query(0, 0, n - 1, start, n - 1)
            ans.append(counts[target_x])

        return ans