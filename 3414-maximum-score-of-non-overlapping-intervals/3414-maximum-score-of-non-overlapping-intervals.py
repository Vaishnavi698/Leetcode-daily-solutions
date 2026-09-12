import sys
from bisect import bisect_right
from functools import lru_cache
from typing import List

# Increase recursion depth for large input sizes
sys.setrecursionlimit(200000)

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        # Store intervals as: (l, r, weight, orig_idx)
        arr = sorted([(l, r, w, i) for i, (l, r, w) in enumerate(intervals)])
        n = len(arr)
        starts = [x[0] for x in arr]

        @lru_cache(None)
        def dp(i: int, count: int):
            if i == n or count == 0:
                return (0, ())

            # Option 1: Skip current interval
            res_weight, res_indices = dp(i + 1, count)

            # Option 2: Take current interval
            l, r, w, idx = arr[i]
            next_idx = bisect_right(starts, r)
            
            next_weight, next_indices = dp(next_idx, count - 1)
            take_weight = w + next_weight
            
            # Key Fix: Sort indices to ensure valid lexicographical order
            take_indices = tuple(sorted((idx,) + next_indices))

            # Compare best total weight, then lexicographical order of sorted index tuples
            if take_weight > res_weight:
                return (take_weight, take_indices)
            elif take_weight == res_weight:
                if not res_indices or take_indices < res_indices:
                    return (take_weight, take_indices)

            return (res_weight, res_indices)

        return list(dp(0, 4)[1])