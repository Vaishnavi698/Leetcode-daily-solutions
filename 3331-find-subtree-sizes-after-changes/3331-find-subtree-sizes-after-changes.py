from typing import List


class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        orig_children: List[List[int]] = [[] for _ in range(n)]
        for i in range(1, n):
            orig_children[parent[i]].append(i)

        new_parent = parent[:]
        last_seen = [-1] * 26

        def reassign(u: int) -> None:
            c = ord(s[u]) - ord("a")
            if last_seen[c] != -1:
                new_parent[u] = last_seen[c]

            prev = last_seen[c]
            last_seen[c] = u
            for v in orig_children[u]:
                reassign(v)
            last_seen[c] = prev

        reassign(0)

        new_children: List[List[int]] = [[] for _ in range(n)]
        for i in range(1, n):
            new_children[new_parent[i]].append(i)

        ans = [0] * n

        def dfs_size(u: int) -> int:
            size = 1
            for v in new_children[u]:
                size += dfs_size(v)
            ans[u] = size
            return size

        dfs_size(0)
        return ans
