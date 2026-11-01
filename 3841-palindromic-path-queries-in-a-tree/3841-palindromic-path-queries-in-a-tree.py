from typing import List

class Solution:
    def palindromePath(self, n: int, edges: List[List[int]], s: str, queries: List[str]) -> List[bool]:
        return self.palindromicPathQueries(n, edges, s, queries)

    def palindromicPathQueries(self, n: int, edges: List[List[int]], s: str, queries: List[str]) -> List[bool]:
        # Adjacency list representation
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        # 1. Heavy-Light Decomposition setup
        parent = [0] * n
        depth = [0] * n
        heavy = [-1] * n
        head = [0] * n
        pos = [0] * n
        cur_pos = 0
        
        # First DFS to compute subtree sizes, depth, parent, heavy child
        def dfs1(u, p, d):
            parent[u] = p
            depth[u] = d
            size = 1
            max_sub_size = 0
            for v in adj[u]:
                if v != p:
                    sub_size = dfs1(v, u, d + 1)
                    size += sub_size
                    if sub_size > max_sub_size:
                        max_sub_size = sub_size
                        heavy[u] = v
            return size
            
        dfs1(0, -1, 0)
        
        # Second DFS to assign positions and chain heads
        def dfs2(u, h):
            nonlocal cur_pos
            head[u] = h
            pos[u] = cur_pos
            cur_pos += 1
            if heavy[u] != -1:
                dfs2(heavy[u], h)
            for v in adj[u]:
                if v != parent[u] and v != heavy[u]:
                    dfs2(v, v)
                    
        dfs2(0, 0)
        
        # 2. Segment Tree for Range XOR Updates / Point Updates & Path Queries
        tree = [0] * (4 * n)
        
        def update_tree(node, l, r, idx, val):
            if l == r:
                tree[node] = val
                return
            mid = (l + r) // 2
            if idx <= mid:
                update_tree(2 * node, l, mid, idx, val)
            else:
                update_tree(2 * node + 1, mid + 1, r, idx, val)
            tree[node] = tree[2 * node] ^ tree[2 * node + 1]
            
        def query_tree(node, l, r, ql, qr):
            if ql > r or qr < l:
                return 0
            if ql <= l and r <= qr:
                return tree[node]
            mid = (l + r) // 2
            return query_tree(2 * node, l, mid, ql, qr) ^ query_tree(2 * node + 1, mid + 1, r, ql, qr)
            
        # Initialize segment tree with characters
        for i in range(n):
            mask = 1 << (ord(s[i]) - ord('a'))
            update_tree(1, 0, n - 1, pos[i], mask)
            
        # Helper to query path between u and v
        def query_path(u, v):
            res = 0
            while head[u] != head[v]:
                if depth[head[u]] < depth[head[v]]:
                    u, v = v, u
                res ^= query_tree(1, 0, n - 1, pos[head[u]], pos[u])
                u = parent[head[u]]
            if depth[u] > depth[v]:
                u, v = v, u
            res ^= query_tree(1, 0, n - 1, pos[u], pos[v])
            return res

        # Process queries
        answer = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                mask = 1 << (ord(c) - ord('a'))
                update_tree(1, 0, n - 1, pos[u], mask)
            else:
                u, v = int(parts[1]), int(parts[2])
                path_mask = query_path(u, v)
                # Check if at most one bit is set
                is_palindrome = (path_mask & (path_mask - 1)) == 0
                answer.append(is_palindrome)
                
        return answer