#Ques
#You are given a binary string s of length n, where:
#'1' represents an active section.
#'0' represents an inactive section.
#You can perform at most one trade to maximize the number of active sections in s. In a trade, you:Convert a contiguous block of '1's that is surrounded by '0's to all '0's.Afterward, convert a contiguous block of '0's that is surrounded by '1's to all '1's.Additionally, you are given a 2D array queries, where queries[i] = [li, ri] represents a substring s[li...ri].For each query, determine the maximum possible number of active sections in s after making the optimal trade on the substring s[li...ri].Return an array answer, where answer[i] is the result for queries[i].

#Solution

import math

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: list[list[int]]) -> list[int]:
        n = len(s)
        total_ones = s.count('1')
        
        # 1. Identify all zero-groups in the string
        zero_groups = [] # List of tuples: (start_idx, length)
        zero_group_index = [-1] * n
        
        for i in range(n):
            if s[i] == '0':
                if i > 0 and s[i - 1] == '0':
                    start, length = zero_groups[-1]
                    zero_groups[-1] = (start, length + 1)
                else:
                    zero_groups.append((i, 1))
                zero_group_index[i] = len(zero_groups) - 1
            else:
                # If s[i] == '1', it takes the index of the most recent zero group
                zero_group_index[i] = len(zero_groups) - 1

        m = len(zero_groups)
        if m == 0:
            return [total_ones] * len(queries)

        # 2. Precompute merged lengths of adjacent zero groups
        # Merging two adjacent zero groups gives a combined length of (len1 + len2)
        zero_merge_lengths = [
            zero_groups[i][1] + zero_groups[i + 1][1] 
            for i in range(m - 1)
        ]

        # 3. Build Sparse Table for Range Maximum Query on zero_merge_lengths
        st_size = len(zero_merge_lengths)
        if st_size > 0:
            LOG = math.floor(math.log2(st_size)) + 1
            st = [[0] * st_size for _ in range(LOG)]
            for i in range(st_size):
                st[0][i] = zero_merge_lengths[i]
                
            for j in range(1, LOG):
                length = 1 << (j - 1)
                for i in range(st_size - (1 << j) + 1):
                    st[j][i] = max(st[j - 1][i], st[j - 1][i + length])

        def query_st(L, R):
            if L > R or st_size == 0:
                return 0
            j = math.floor(math.log2(R - L + 1))
            return max(st[j][L], st[j][R - (1 << j) + 1])

        ans = []
        for l, r in queries:
            # Calculate remaining zero length at left boundary l
            left = 0
            if zero_group_index[l] != -1:
                g_start, g_len = zero_groups[zero_group_index[l]]
                left = g_len - (l - g_start)

            # Calculate remaining zero length at right boundary r
            right = 0
            if zero_group_index[r] != -1:
                g_start, _ = zero_groups[zero_group_index[r]]
                right = r - g_start + 1

            # Determine inner adjacent zero group range
            start_adj = zero_group_index[l] + 1
            end_adj = (zero_group_index[r] if s[r] == '1' else zero_group_index[r] - 1) - 1

            active_sections = total_ones

            # Option A: Both boundaries l and r fall inside adjacent zero groups
            if s[l] == '0' and s[r] == '0' and zero_group_index[l] + 1 == zero_group_index[r]:
                active_sections = max(active_sections, total_ones + left + right)
            
            # Option B: Trade completely within the fully contained range
            if start_adj <= end_adj:
                active_sections = max(active_sections, total_ones + query_st(start_adj, end_adj))

            # Option C: Trade merging the left boundary zero group with the next zero group
            if s[l] == '0':
                limit = zero_group_index[r] if s[r] == '1' else zero_group_index[r] - 1
                if zero_group_index[l] + 1 <= limit:
                    next_len = zero_groups[zero_group_index[l] + 1][1]
                    active_sections = max(active_sections, total_ones + left + next_len)

            # Option D: Trade merging the right boundary zero group with the previous zero group
            if s[r] == '0' and zero_group_index[l] < zero_group_index[r] - 1:
                prev_len = zero_groups[zero_group_index[r] - 1][1]
                active_sections = max(active_sections, total_ones + right + prev_len)

            ans.append(active_sections)

        return ans